# world-places

Official population figures for places the World Bank's API leaves out (Taiwan, Jersey, Åland, Cook Islands, ...), from each
place's own statistics office, one JSON per source, published weekly to Hugging Face
([dataset](https://huggingface.co/datasets/milleleaf/world-places), [bucket](https://huggingface.co/buckets/milleleaf/world-places)
read by browsers) and mirrored to [Kaggle](https://www.kaggle.com/datasets/helenkwok/world-places). Built from
[pipeline-template](https://github.com/milleleaf/pipeline-template).

Why a pipeline: some sources cannot be read from a browser (Åland's PxWeb answers only a JSON POST and refuses the CORS
preflight; Jersey's open data sends no CORS header). Official figures with no open licence (Guernsey, Northern Cyprus, Anguilla, Montserrat, Saint Helena and Tristan da Cunha,
Falklands, Vatican, Somaliland) are republished as facts with credit (Helen, 2026-10-10) in a separate dataset,
`alreadyopen/world-places-nc` (bake.py `NC`, written to `data/out/nc/`, published with `EDITION=nc python3 publish.py`), and
only the separate nc site reads them; the open dataset holds open-licence sources only. Western Sahara is covered only by Morocco's two
regions (`morocco_hcp`), side by side and never summed; Somaliland (`somaliland_manual`) is typed in by hand from a PDF and
rechecked yearly. Places with no official source at all are not in here; the map shows Natural Earth's estimate for them,
labelled as such.

    python3 bake.py [<source id> ...]                # data/out/<source>.json + index.json
    python3 publish.py                               # gate, then Hugging Face (HF_TOKEN)
    python3 check.py                                 # data-free checks (CI)

Add a source: a function in `bake.py` returning `[{iso3, name, population, period, ...}]`, an entry in `SOURCES` (plus `NOLIC`
when the source states no open licence) and in `sources.json`, and a row in `hf/README.md` crediting the owner.
