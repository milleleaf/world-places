---
pretty_name: World places (official figures for places the World Bank leaves out)
license: other
license_name: per-source
license_link: https://github.com/milleleaf/world-places/blob/main/sources.json
tags:
  - geospatial
  - population
  - official-statistics
---

# World places

Official population figures for places that the World Bank's API leaves out, each from the place's own statistics office
(or the official regional body), rebuilt weekly by [AlreadyOpen/world-places](https://github.com/milleleaf/world-places).
Taiwan, for example, has its own government and population and no World Bank entry at all.

- `index.json`: the bake time, the files, and how many places each holds.
- `<source>.json`, one per source, never merged, so each keeps its own terms: `publisher`, `url`, `licence`, and `places`
  with `iso3`, `name`, `population`, `period`, and where the source publishes it, `aged_65_plus_pct` and `density_per_km2`.
  A figure a source does not publish is left out, never estimated.
- `countries.pmtiles` (bucket and dataset): Natural Earth 1:10m country outlines (public domain) as vector tiles, layer
  `countries`, zooms 0-10, every Natural Earth field. Taiwan, Hong Kong and Macau are their own places.
- `manifest.json`: sha256 and size of every file, the counts and the sources.

| File | Places | Publisher | Terms |
|---|---|---|---|
| `taiwan.json` | Taiwan | Ministry of the Interior (Taiwan), Department of Household Registration | [Open Government Data License](https://data.gov.tw/license) |
| `pacific.json` | Cook Islands, Niue, Wallis and Futuna, Pitcairn Islands | Pacific Community (SPC) | [terms of use](https://pacificdata.org/terms-of-use) |
| `aland.json` | Åland | Statistics and Research Åland (ÅSUB). Källa: ÅSUB | [CC BY 4.0](https://www.asub.ax/sv/om-asub/om-asubax/anvandarvillkor) |
| `norfolk.json` | Norfolk Island | Australian Bureau of Statistics | [CC BY 4.0](https://www.abs.gov.au/website-privacy-copyright-and-disclaimer) |
| `insee.json` | Saint Pierre and Miquelon, Saint-Barthélemy, Saint-Martin | INSEE. Source : Insee | [Licence Ouverte 2.0](https://www.insee.fr/fr/information/2008466) |
| `jersey.json` | Jersey | Statistics Jersey | [Open Government Licence – Jersey v1.0](https://www.gov.je/ServiceManual/opendata/Pages/open-government-licence-jersey-ogl-j-v1-0.aspx) |
| `morocco_hcp.json` | Laâyoune-Sakia El Hamra, Dakhla-Oued Ed-Dahab (`ESH`) | Haut-Commissariat au Plan (HCP), Morocco. Source : HCP, RGPH 2024 | [CC BY 4.0 for indicators](https://www.hcp.ma/Conditions-generales-d-utilisation-Version-1-0_a2194.html) |

Every file here is under an open licence or open terms. Official figures with no open licence (Guernsey, Northern Cyprus,
Anguilla, Montserrat, Saint Helena and Tristan da Cunha, Falklands, Vatican, Somaliland) are in a separate dataset,
[alreadyopen/world-places-nc](https://huggingface.co/datasets/milleleaf/world-places-nc). Places may carry `notes`
(estimate caveats). `morocco_hcp.json` gives Morocco's 2024 census legal population for the two Moroccan-administered regions
side by side, with `scope` and `status_note` ("Status disputed"): Morocco's regional borders do not match the territory of
Western Sahara, so they are never summed into a Western Sahara total.

Taiwan's density uses its land area of 36,197 km² (Ministry of the Interior). The 65+ share is computed from each source's
single-year age counts. Provided as is, with no warranty, and not endorsed by any of the sources.
