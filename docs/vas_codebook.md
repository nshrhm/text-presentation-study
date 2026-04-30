# VAS Codebook

This codebook records the information needed to interpret the Visual Analog Scale variables in `src/data_all.csv`.

## Current Status

The public CSV contains normalized 0-100 values for the following variables:

- `readability`
- `stress`
- `understanding`
- `memorability`

The manuscript should not be submitted until the original questionnaire and/or logging code confirm the exact item wording, anchors, default slider position, and scoring direction for every item.

## Required Item-Level Documentation

| Variable | Construct | Raw scale | Normalized scale | Higher values currently treated as | Status |
| --- | --- | --- | --- | --- | --- |
| `readability` | Perceived readability | 0-1000 | 0-100 | More readable | Needs anchor verification |
| `stress` | Perceived stress | 0-1000 | 0-100 | More stress | Critical: scoring direction must be verified |
| `understanding` | Self-reported ease of understanding | 0-1000 | 0-100 | Greater perceived understanding | Needs anchor verification |
| `memorability` | Perceived memorability | 0-1000 | 0-100 | Greater perceived memorability | Needs anchor verification |

## Stress Coding Risk

The static UI example in `src/sample_ui_en.html` shows the stress slider with the left anchor "Unbearable stress" and the right anchor "No stress at all". If the original experimental application used the same left-to-right coding without reverse coding, higher numeric values would mean less stress. The current analysis treats higher values as greater stress. This must be resolved from the original Unity project or raw export documentation before the stress result is publishable.

## Submission Requirement

Before journal submission, add a table to the manuscript with:

- exact item wording
- left and right anchors
- raw scale range
- normalized scale range
- default slider position
- scoring direction
- reverse-coding procedure, if used
