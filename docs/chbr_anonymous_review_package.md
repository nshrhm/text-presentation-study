# CHBR Anonymous Review Package Plan

This public repository is useful for open inspection, but it is not suitable as the repository linked from an anonymized CHBR manuscript. The public GitHub owner, title page, declaration files, rebuttal drafts, revision plans, and project history can compromise double-anonymized review.

## Use for CHBR Review

Create a separate anonymized supplementary package or anonymized review repository containing only the files needed to reproduce the analysis and inspect the study materials:

- anonymized manuscript source and PDF
- anonymized figures used in the manuscript
- `src/data_all.csv`
- `src/study_analysis.py`
- `src/analyze_data.py`
- `src/visualize_data.py`
- `docs/data_dictionary.md`
- `docs/analysis_results.md`
- `docs/vas_codebook.md`
- `docs/stimulus_source.md`
- `docs/reproducibility.md`
- `paper/highlights.md`
- `paper/refworks.bib`

## Exclude From Anonymous Review

Do not include:

- `backup/`
- `paper/title_page.tex` or `paper/title_page.pdf`
- `paper/declarations.md` if it contains author-identifying CRediT or conflict details
- `docs/rebuttal_round1.md`
- `docs/chbr_revision_plan.md`
- `docs/publication_checklist.md`
- `docs/log.md` if it reveals internal revision history
- `.git/` history
- GitHub owner names, author names, affiliations, or acknowledgements
- local build products such as `.aux`, `.bbl`, `.blg`, `.log`, and `.spl`

## Data Availability Wording During Review

Use wording that does not reveal author identity:

> For double-anonymized review, the de-identified participant-level dataset and analysis code are provided as anonymized supplementary materials. A public repository link and persistent dataset citation will be supplied after review.

## Data Availability Wording After Review

After review anonymity is no longer required, replace the review statement with a public repository or dataset DOI:

> The de-identified participant-level dataset and analysis code supporting this study are publicly available at [repository or DOI].
