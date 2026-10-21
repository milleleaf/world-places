---
pretty_name: World places, credited (official figures with no open licence)
license: other
license_name: per-source-no-open-licence
license_link: https://github.com/milleleaf/world-places/blob/main/sources.json
tags:
  - population
  - official-statistics
---

# World places, credited (no open licence)

Official population figures for places the World Bank's API leaves out, from statistics offices that publish them under
plain copyright or with no licence stated. They are republished as facts, each credited to its publisher with a link to
its own page, and kept apart from the open-licence dataset [alreadyopen/world-places](https://huggingface.co/datasets/milleleaf/world-places).
Rebuilt weekly by [AlreadyOpen/world-places](https://github.com/milleleaf/world-places).

**Terms:** no open licence. Each file names its publisher and links its terms where one exists; check them before reuse.
Somaliland's figure is entered by hand from its PDF. Western Sahara is not here: Morocco HCP's regional figures are CC BY 4.0
and sit in the open dataset.

- `index.json`, `<source>.json` (one per source, never merged), `manifest.json`. Each file carries `"licence_note"`.
- Northern Cyprus and Somaliland use Natural Earth's codes `CYN` and `SOL`. `saint_helena.json` holds Tristan da Cunha as a
  sub-place `SHN-TA` with its own `publisher` and `url` (Ascension publishes no figures). `somaliland_manual.json` is entered
  by hand from the PDF (`entered_by_hand` says when) and rechecked yearly.

| File | Places | Publisher | Terms |
|---|---|---|---|
| `guernsey.json` | Guernsey | States of Guernsey Data & Analysis | no open licence stated; facts republished with credit ([source](https://www.gov.gg/population)) |
| `northern_cyprus.json` | Northern Cyprus (`CYN`) | TRNC Statistical Institute (İstatistik Kurumu) | no open licence stated ([terms of use](https://stat.gov.ct.tr/Terms)) |
| `anguilla.json` | Anguilla | Anguilla Statistics Department | no open licence stated ([source](https://statistics.gov.ai/AllDocuments/1.1%20Population.xlsx)) |
| `montserrat.json` | Montserrat | Statistics Department Montserrat, Ministry of Finance and Economic Management | no open licence stated ([source](https://statistics.gov.ms/)) |
| `saint_helena.json` | Saint Helena; Tristan da Cunha (`SHN-TA`) | St Helena Government Statistics Office; Tristan da Cunha Association (Tristan) | no open licence stated ([St Helena](https://www.sainthelena.gov.sh/st-helena/statistics/), [Tristan](https://tristandc.com/population.php)) |
| `falklands.json` | Falkland Islands | Falkland Islands Government, Policy Department | no open licence stated ([source](https://www.gov.fk/policy/)) |
| `vatican.json` | Vatican City | Governatorato dello Stato della Città del Vaticano | no open licence stated ([source](https://www.vaticanstate.va/it/stato-e-governo/note-generali/popolazione.html)) |
| `somaliland_manual.json` | Somaliland (`SOL`) | Central Statistics Department, Ministry of Planning and National Development, Somaliland | no open licence stated ([PDF](https://somalilandcsd.org/wp-content/uploads/2022/12/A5-CSD_SOMALILAND-IN-FIGURES.pdf)) |

Provided as is, with no warranty, and not endorsed by any of the sources.
