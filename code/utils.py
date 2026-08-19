"""
utils.py

Shared paths, variable names, and constants for the rural-mobility project.
Imported at the top of every notebook so that no path or key variable name is
hardcoded in more than one place.
"""

import os

## every path is resolved relative to this file, so the notebooks run
## unchanged on any machine and from any working directory
CODE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_DIR = os.path.dirname(CODE_DIR)
DATA_DIR = os.path.join(PROJ_DIR, "data")
OUT_DIR = os.path.join(PROJ_DIR, "output")

## ---- raw data sources (Opportunity Insights Atlas, public download) ----
DATA_SOURCES = {
    ## Atlas table 4: tract-level outcomes for the 1978-83 birth cohorts
    "tract_outcomes_simple.csv":
        "https://opportunityinsights.org/wp-content/uploads/2018/10/tract_outcomes_simple.csv",
    ## Atlas table 9: tract-level neighborhood characteristics
    "tract_covariates.csv":
        "https://opportunityinsights.org/wp-content/uploads/2018/10/tract_covariates.csv",
}

## ---- key variables ----
ID_COLS = ["state", "county", "tract"]
MOBILITY_VAR = "kfr_pooled_pooled_p25"  # mean adult HH income rank, kids w/ p25 parents
COUNT_VAR = "pooled_pooled_count"       # n children behind each tract estimate

## rural threshold, people per square mile in 2000
RURAL_CUTOFF = 100
DENSE_URBAN_CUTOFF = 10000
MIN_CHILD_COUNT = 200

## density cut points (people per sq. mile, Census 2000) and their labels
DENSITY_BINS = [float("-inf"), 100, 500, 2000, 10000, float("inf")]
DENSITY_LABELS = ["Rural\n(<100)", "Small town\n(100-500)", "Suburban\n(500-2k)",
                  "Urban\n(2k-10k)", "Dense urban\n(10k+)"]

## neighborhood characteristics compared between high- and low-mobility rural tracts
COVARIATES = {
    "singleparent_share2000": "Share single-parent households",
    "poor_share2000": "Share below poverty line",
    "mean_commutetime2000": "Mean commute time",
    "ann_avg_job_growth_2004_2013": "Annual job growth, 2004-13",
    "mail_return_rate2010": "Census mail return rate",
    "gsmn_math_g3_2013": "Mean 3rd-grade math score",
    "hhinc_mean2000": "Mean household income",
    "emp2000": "Share of adults employed",
    "frac_coll_plus2000": "Share with a BA or higher",
    "share_white2000": "Share white",
}

## ---- figure palette (light surface) ----
BLUE = "#2a78d6"
ORANGE = "#eb6834"
INK = "#0b0b0b"
INK_MUTED = "#52514e"
GRID = "#d8d7d2"


def data_path(filename):
    """Absolute path to a file in data/."""
    return os.path.join(DATA_DIR, filename)


def output_path(filename):
    """Absolute path to a file in output/."""
    return os.path.join(OUT_DIR, filename)
