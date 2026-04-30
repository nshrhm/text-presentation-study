# Reproducibility Guide

This guide describes how to reproduce the reviewer-facing artifacts in this repository.

## Environment

The analysis and visualization scripts require Python 3 and the packages listed in `requirements.txt`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Regenerate Statistical Results

Run the statistical analysis script from the repository root:

```bash
python src/analyze_data.py
```

By default, the script reads `src/data_all.csv` and writes:

- `docs/analysis_results.md`
- `docs/analysis_results.json`

The generated results include descriptive statistics, Levene tests, independent-samples t-tests, and Cohen's d.

## Regenerate Figures

Run the visualization script from the repository root:

```bash
python src/visualize_data.py
```

By default, the script reads `src/data_all.csv` and writes the English manuscript figures to `paper/images/`:

- `paper/images/subjective_en.png`
- `paper/images/subjective_en.pdf`
- `paper/images/time_en.png`
- `paper/images/time_en.pdf`

To choose a different dataset or output directory:

```bash
python src/visualize_data.py --data src/data_all.csv --output-dir paper/images
```

## Full Analysis Run

From the repository root:

```bash
python src/test_imports.py
python src/analyze_data.py
python src/visualize_data.py
```

## Compile the Manuscript

The repository includes `paper/main.pdf` for direct reviewer inspection. To rebuild the PDF locally, use a LaTeX environment with `elsarticle` support:

```bash
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The generated LaTeX build products are intentionally ignored by Git.

## Expected Inputs

- `paper/main.tex`
- `paper/refworks.bib`
- `paper/images/subjective_en.pdf`
- `paper/images/time_en.pdf`
- `paper/images/ls_en.png`
- `paper/images/vas_en.png`

## Validation Notes

The `v1.0.0` release was checked by running:

```bash
python3 -m py_compile src/study_analysis.py src/analyze_data.py src/visualize_data.py src/test_imports.py
python3 src/test_imports.py
python3 src/analyze_data.py
python3 src/visualize_data.py
```

The manuscript PDF was rebuilt with `pdflatex`, `bibtex`, and two final `pdflatex` passes. The LaTeX log was checked for unresolved citation and reference warnings.

## Build the Separate Title Page

```bash
cd paper
pdflatex title_page.tex
```

The title page contains author-identifying information and must be submitted separately from the anonymized manuscript.

## Publication Boundary

Do not publish or commit `backup/`. It contains private development notes and is not part of the reviewer package.
