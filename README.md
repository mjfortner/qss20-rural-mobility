# Which rural places move kids up?

**QSS 20 final project — Max Fortner (solo).** Project option: Senior Thesis / Own Data.

**Research question:** what distinguishes rural Census tracts with above-average upward
mobility from otherwise similar rural tracts with below-average mobility?

Using the Opportunity Insights Opportunity Atlas, I merge tract-level upward-mobility
outcomes for the 1978–1983 birth cohorts onto tract-level neighborhood characteristics
(74k tracts), and fit an OLS model of mobility on those characteristics among the
17.3k rural tracts. Mobility varies more *within* density categories than between them,
and among rural tracts the share of single-parent households is by far the strongest
correlate — about 2.5x the next-largest standardized coefficient.

![Mobility varies widely within every density category](output/fig1_mobility_by_density.png)

![Single-parent share dominates rural mobility differences](output/fig2_rural_ols_coefficients.png)

## Code

Run the notebooks in numeric order. Each defines its functions at the top and imports
shared paths and variable names from [`code/utils.py`](code/utils.py), so no path is
hardcoded to one machine.

| Notebook | Takes in | Does | Outputs |
|---|---|---|---|
| [`code/00_pull.ipynb`](code/00_pull.ipynb) | — (downloads from the web) | Downloads the two Opportunity Insights Atlas tables into `data/`, skipping files already present. Prints row counts, duplicate-id checks, and missingness on the key fields. | `data/tract_outcomes_simple.csv`, `data/tract_covariates.csv` |
| [`code/01_merge.ipynb`](code/01_merge.ipynb) | `data/tract_outcomes_simple.csv`, `data/tract_covariates.csv` | Inner-joins outcomes onto covariates on `(state, county, tract)` with row counts printed before and after, drops tracts with no mobility estimate or no density, bins density into five categories, flags tracts above the national median, and tabulates missingness in every key field. | `data/analysis_sample.csv`, `output/table2_missingness.tex` |
| [`code/02_analyze.ipynb`](code/02_analyze.ipynb) | `data/analysis_sample.csv` | Fits OLS of mobility on standardized neighborhood characteristics among rural tracts, with a logistic model of the above-median indicator as a robustness check, and builds the figures and tables. | `output/fig1_mobility_by_density.png`, `output/fig2_rural_ols_coefficients.png`, `output/table1_analysis_sample.tex`, `output/table3_ols_results.tex` |
| [`code/utils.py`](code/utils.py) | — | Shared paths, data-source URLs, key variable names, density bins, covariate list, figure palette. | — |

Requires `pandas`, `numpy`, `matplotlib`, and `statsmodels`.

## Data

Not committed — see [`data/README.md`](data/README.md) for the download links.
`00_pull.ipynb` fetches both raw files automatically.

- **Source:** [Opportunity Insights Opportunity Atlas](https://opportunityinsights.org/data/), tables 4 and 9
- **Unit of analysis:** 2010 Census tract, keyed to where a child grew up
- **Time window:** outcomes for the 1978–1983 birth cohorts measured in adulthood
  (~2014–2015) from federal tax records; covariates measured in 2000 except where the
  variable name says otherwise
- **Primary outcome:** `kfr_pooled_pooled_p25` — mean adult household income rank for
  children whose parents were at the 25th percentile
- **Rural definition:** fewer than 100 people per square mile in 2000
- **Missingness:** ~1% on most fields, 1.6% on the mobility outcome (Opportunity Insights
  suppresses tracts with too few children). Quantified per field in
  `output/table2_missingness.tex`; models are fit on complete cases.

## Output

| File | What it is |
|---|---|
| [`output/fig1_mobility_by_density.png`](output/fig1_mobility_by_density.png) | Distribution of tract mobility across five population-density categories |
| [`output/fig2_rural_ols_coefficients.png`](output/fig2_rural_ols_coefficients.png) | OLS coefficients per SD with 95% CIs, rural tracts only |
| `output/table1_analysis_sample.tex` | Sample characterization |
| `output/table2_missingness.tex` | Missingness by field, nationally and among rural tracts |
| `output/table3_ols_results.tex` | Full OLS results |

## Writeup

[`writeup/milestone1_fortner.pdf`](writeup/milestone1_fortner.pdf) — Milestone 1 memo
(source: [`writeup/milestone1_fortner.tex`](writeup/milestone1_fortner.tex)).

## Caveats

Descriptive associations on cross-sectional tract data, not causal estimates. The
covariates are heavily collinear — conditioning on single-parent share flips the poverty
and household-income coefficients against their bivariate signs — so the model is better
read as separating one "family structure and disadvantage" dimension than ten
independent predictors.
