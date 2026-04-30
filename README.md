# Text Presentation Study

Version: 1.0.0

This repository contains the manuscript source, anonymized study data, and figure-generation code for an academic study comparing two text presentation methods in web-based interfaces:

- character-by-character text presentation
- immediate full-text presentation

The repository is a public research package for inspecting the analysis materials, reproducing the figures, and understanding the experimental design without relying on private development notes. It is not an anonymized CHBR review repository because the public GitHub owner and some repository files may identify the authors or internal revision history.

## Study Summary

The study used a between-subjects design with 24 participants. Group A viewed text through character-by-character presentation, and Group B viewed the same text as full text. Participants evaluated readability, stress, understanding, and memorability using Visual Analog Scale ratings. Reading time was recorded as an objective measure.

The manuscript reports that completion time remained significant after Holm correction across five exploratory outcomes. Stress and self-reported ease of understanding differed only before correction, while readability and perceived memorability did not show clear group differences.

## Repository Contents

| Path | Purpose |
| --- | --- |
| `paper/main.tex` | Main LaTeX manuscript source. |
| `paper/main.pdf` | Compiled anonymized manuscript for reviewer inspection. |
| `paper/title_page.tex` | Separate title page with author information. |
| `paper/highlights.md` | CHBR-style highlights file. |
| `paper/declarations.md` | Submission declarations requiring author confirmation. |
| `paper/refworks.bib` | Bibliography database used by the manuscript. |
| `paper/images/` | English figures used in the manuscript. |
| `src/data_all.csv` | Anonymized participant-level dataset used for visualization. |
| `src/study_analysis.py` | Shared dataset validation and statistical analysis utilities. |
| `src/analyze_data.py` | Script for regenerating statistical results in Markdown and JSON. |
| `src/visualize_data.py` | Script for regenerating manuscript figures. |
| `src/sample_ui_en.html` | Static example of the English questionnaire UI. |
| `docs/experimental_plan.md` | Experimental design and reviewer-facing protocol notes. |
| `docs/data_dictionary.md` | Variable definitions and coding notes for the CSV dataset. |
| `docs/analysis_results.md` | Regenerated descriptive and inferential statistics. |
| `docs/vas_codebook.md` | VAS scoring documentation and unresolved coding checks. |
| `docs/stimulus_source.md` | Source metadata for the reading stimulus. |
| `docs/chbr_revision_plan.md` | CHBR-focused revision status and remaining blockers. |
| `docs/chbr_anonymous_review_package.md` | Plan for a double-anonymized CHBR review package. |
| `docs/rebuttal_round1.md` | Draft response to reviewers based on the current revision. |
| `docs/reproducibility.md` | Reproduction steps for figures and manuscript build. |
| `docs/publication_checklist.md` | Public-release audit checklist. |
| `docs/log.md` | Public project log for reviewer orientation. |

## Reviewer Quick Start

1. Read the compiled manuscript at `paper/main.pdf`.
2. Inspect the dataset definition in `docs/data_dictionary.md`.
3. Inspect regenerated statistics in `docs/analysis_results.md`.
4. Reproduce statistics and figures using the instructions in `docs/reproducibility.md`.
5. Review the experimental design notes in `docs/experimental_plan.md`.

## Privacy and Publication Boundary

The `backup/` directory contains private development notes and must not be published. It is intentionally excluded through `.gitignore`. Public documentation, code comments, and reviewer-facing materials in this repository should be written in English.

The public dataset in `src/data_all.csv` contains anonymized participant-level measurements and does not include names, contact details, or direct identifiers.

## Submission Readiness

This repository now contains a more cautious exploratory manuscript package, but it is not ready for CHBR submission until the unresolved ethics approval/waiver details, remaining stimulus display details, participant demographics, and declaration fields are confirmed. For double-anonymized CHBR review, use a stripped anonymized supplement or review repository rather than linking to this public repository.

## License

No reuse license has been selected for this unpublished manuscript package. Until a license is added, copyright remains with the authors and GitHub's default terms apply.
