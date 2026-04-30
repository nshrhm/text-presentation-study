# Publication Checklist

This checklist records the repository-level checks performed before the `v1.0.0` public release.

## Completed Checks

- `backup/` is excluded by `.gitignore`.
- Local assistant/editor state is excluded by `.gitignore`.
- Localized Japanese draft artifacts are excluded by `.gitignore`.
- LaTeX build products are excluded by `.gitignore`.
- Public repository documentation is written in English.
- Public dataset contains anonymized participant-level measurements only.
- Analysis scripts run from the repository root.
- Statistical analysis outputs are regenerated from `src/data_all.csv`.
- Manuscript figures are regenerated from `src/data_all.csv`.
- `paper/main.pdf` is rebuilt from `paper/main.tex`.
- LaTeX build log contains no unresolved citation or reference warnings.
- The main manuscript file has no author names or affiliations, but this public repository is not itself suitable for double-anonymized CHBR review.
- A separate title page file has been added.
- CHBR-style highlights and declaration files have been added.
- VAS scoring risks are documented in `docs/vas_codebook.md`.
- A CHBR anonymous review package plan is documented in `docs/chbr_anonymous_review_package.md`.

## Publication Notes

This repository is intended as a reviewer-facing research package for an unpublished manuscript. No private development notes from `backup/` are part of the release.

For CHBR double-anonymized review, do not link directly to this public GitHub repository from the anonymized manuscript. Use an anonymized supplementary package or anonymized review repository.

No reuse license has been selected in this release. Until a license is added, copyright remains with the authors and GitHub's default terms apply.

## Remaining Submission Blockers

- Ethics approval or waiver details remain unresolved and require institutional confirmation before journal submission.
- Stress VAS scoring direction has been verified from the source manuscript and author-confirmed anchors.
- Stimulus source metadata is documented in `docs/stimulus_source.md`; exact excerpt length, line breaks, font, display details, and total reveal duration remain unavailable in the public analysis record unless recovered from original materials.
- Participant recruitment, demographics, randomization, compensation, and group balance details must be completed.
- Competing interests, CRediT roles, and final author approval of the generative-AI declaration must be completed.
