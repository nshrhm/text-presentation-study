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

Levene's test uses mean-centered variance comparison. Independent-samples t-tests use equal variances when Levene's test is not significant at alpha = 0.05.

| Measure | Variance | Test | df | t | p | Cohen's d |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| Readability | Homogeneous | Student t-test | 22.00 | -0.97 | 0.3443 | -0.39 |
| Stress | Homogeneous | Student t-test | 22.00 | 2.62 | 0.0155 | 1.07 |
| Understanding | Homogeneous | Student t-test | 22.00 | 2.14 | 0.0441 | 0.87 |
| Memorability | Homogeneous | Student t-test | 22.00 | -0.34 | 0.7400 | -0.14 |
| Time (seconds) | Homogeneous | Student t-test | 22.00 | 3.41 | 0.0025 | 1.39 |
