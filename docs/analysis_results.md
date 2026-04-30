# Analysis Results

This file is generated from `src/data_all.csv` by `src/analyze_data.py`.

Input dataset: `src/data_all.csv`

## Descriptive Statistics

### Group A (Character-by-character)

| Measure | Minimum | Median | Mean | Maximum | SD |
| --- | ---: | ---: | ---: | ---: | ---: |
| Readability | 13.00 | 28.00 | 35.42 | 77.00 | 22.58 |
| Stress | 22.00 | 65.50 | 65.25 | 91.00 | 20.05 |
| Understanding | 0.00 | 41.50 | 40.25 | 72.00 | 18.89 |
| Memorability | 9.00 | 27.50 | 34.67 | 80.00 | 21.78 |
| Time (seconds) | 75.30 | 76.53 | 80.87 | 106.85 | 10.04 |

### Group B (Full text)

| Measure | Minimum | Median | Mean | Maximum | SD |
| --- | ---: | ---: | ---: | ---: | ---: |
| Readability | 26.00 | 36.50 | 43.17 | 79.00 | 16.17 |
| Stress | 0.00 | 41.50 | 42.08 | 88.00 | 23.11 |
| Understanding | 11.00 | 24.50 | 26.08 | 59.00 | 13.10 |
| Memorability | 12.00 | 37.50 | 37.25 | 61.00 | 15.32 |
| Time (seconds) | 24.98 | 51.96 | 58.21 | 109.12 | 20.72 |

## Inferential Statistics

All inferential tests are exploratory. Welch's independent-samples t-tests are reported as the primary parametric comparison for robustness to unequal variances. Holm-adjusted p-values control the family-wise error rate across the five outcomes.

| Measure | Mean A | Mean B | A-B | 95% CI | Welch p | Holm p | Hedges g | g 95% CI |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| Readability | 35.42 | 43.17 | -7.75 | [-24.48, 8.98] | 0.3454 | 0.6907 | -0.38 | [-1.46, 0.36] |
| Stress | 65.25 | 42.08 | 23.17 | [4.83, 41.50] | 0.0157 | 0.0627 | 1.03 | [0.27, 2.23] |
| Understanding | 40.25 | 26.08 | 14.17 | [0.31, 28.03] | 0.0456 | 0.1367 | 0.84 | [0.09, 2.19] |
| Memorability | 34.67 | 37.25 | -2.58 | [-18.63, 13.46] | 0.7404 | 0.7404 | -0.13 | [-1.13, 0.60] |
| Time (seconds) | 80.87 | 58.21 | 22.67 | [8.57, 36.77] | 0.0036 | 0.0180 | 1.34 | [0.51, 3.19] |

## Robustness and Assumption Checks

| Measure | Levene p | Shapiro A p | Shapiro B p | Mann-Whitney p | Permutation p | BH p |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Readability | 0.2538 | 0.0154 | 0.0731 | 0.0883 | 0.3450 | 0.4317 |
| Stress | 0.7479 | 0.6098 | 0.9991 | 0.0152 | 0.0172 | 0.0392 |
| Understanding | 0.2466 | 0.9742 | 0.0892 | 0.0376 | 0.0450 | 0.0760 |
| Memorability | 0.3310 | 0.0780 | 0.8717 | 0.4022 | 0.7429 | 0.7404 |
| Time (seconds) | 0.0944 | 0.0001 | 0.0781 | 0.0029 | 0.0021 | 0.0180 |

## Sensitivity Power Analysis

With 12 participants per group and alpha = 0.05, the design has estimated power of 0.47 for Cohen's d = 0.8 in a two-sided independent-samples t-test.
The estimated standardized mean difference required for 80% power is d = 1.20.
