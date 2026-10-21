"""Publish sources.OUT to Hugging Face (needs HF_TOKEN with write access to the alreadyopen org):
  dataset  REPO  DATASET_FILES + manifest.json + the card (hf/README.md): one commit a run, versioned (data tools)
  bucket   REPO  BUCKET_FILES + manifest.json, overwritten in place (read by browsers: CORS + HTTP Range)
Nothing is uploaded unless the publish gate passes (manifest.py). One file per source licence: never merge data under
different terms (e.g. ODbL share-alike with government open data) into one file.
Usage: python3 publish.py     (after bake.py)"""
import json, os
from huggingface_hub import HfApi, batch_bucket_files, create_bucket
import manifest, sources

# Two datasets from one bake: open sources (world-places) and the no-open-licence ones (world-places-nc, bake.NC).
EDITIONS = {
    'open': ('milleleaf/world-places', sources.OUT, 'hf/README.md', ['countries.pmtiles'],
             ('helenkwok/world-places', 'Milleleaf: World places (official figures)')),
    'nc': ('milleleaf/world-places-nc', os.path.join(sources.OUT, 'nc'), 'hf/README-nc.md', [],
           ('helenkwok/world-places-nc', 'Milleleaf: World places nc (credited)')),
}
ED = os.environ.get('EDITION', 'open')
REPO, OUT, CARD, TILES, KAGGLE = EDITIONS[ED]
_idx = os.path.join(OUT, 'index.json')
DATASET_FILES = ['index.json'] + TILES + (json.load(open(_idx))['files'] if os.path.exists(_idx) else [])   # one JSON per source
BUCKET_FILES = DATASET_FILES                                          # small JSON: the map reads the bucket


def main():
    o = lambda f: os.path.join(OUT, f); idx = json.load(open(o('index.json')))
    m = manifest.manifest(OUT, sorted(set(DATASET_FILES + BUCKET_FILES)), idx['counts'], idx['built'])
    url = f'https://huggingface.co/buckets/{REPO}/resolve/manifest.json'
    old = manifest.published(url)
    manifest.gate(m, url)
    json.dump(m, open(o('manifest.json'), 'w'), indent=1)
    gone = sorted(set((old or {}).get('files', {})) - set(m['files']))       # files this edition no longer has (gate allowed it)
    api = HfApi(); api.create_repo(REPO, repo_type='dataset', exist_ok=True)
    for f in DATASET_FILES + ['manifest.json']:
        api.upload_file(path_or_fileobj=o(f), path_in_repo=f, repo_id=REPO, repo_type='dataset', commit_message=f"{f}: bake of {idx['built']}")
    for f in gone:
        api.delete_file(f, repo_id=REPO, repo_type='dataset', commit_message=f'{f}: no longer in this dataset')
    api.upload_file(path_or_fileobj=os.path.join(os.path.dirname(os.path.abspath(__file__)), CARD), path_in_repo='README.md', repo_id=REPO, repo_type='dataset', commit_message='card')
    create_bucket(REPO, private=False, exist_ok=True)
    batch_bucket_files(REPO, add=[(o(f), f) for f in BUCKET_FILES] + [(o('manifest.json'), 'manifest.json')], delete=gone)   # the gate reads the bucket's
    print(json.dumps({'dataset': f'https://huggingface.co/datasets/{REPO}', 'bucket': f'https://huggingface.co/buckets/{REPO}', 'built': idx['built'], 'counts': m['counts'], 'removed': gone}))

if __name__ == '__main__':
    main()
