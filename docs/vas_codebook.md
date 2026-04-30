# VAS Codebook

This codebook records the information needed to interpret the Visual Analog Scale variables in `src/data_all.csv`.

## Current Status

The public CSV contains normalized 0-100 values for the following variables:

- `readability`
- `stress`
- `understanding`
- `memorability`

The Japanese source manuscript `original.pdf` states that participants answered by moving a slider where the left endpoint was 100 and the right endpoint was 0. This supports the current interpretation that higher stress values indicate greater stress if the original experimental application used the same anchors shown in the source manuscript. The original Unity project or raw logging code should still be checked before submission.

## Required Item-Level Documentation

| Variable | Construct | Raw scale | Normalized scale | Higher values currently treated as | Status |
| --- | --- | --- | --- | --- | --- |
| `readability` | Perceived readability | 0-1000 | 0-100 | More readable | Source manuscript supports left=100/right=0; exact anchors still needed |
| `stress` | Perceived stress | 0-1000 | 0-100 | More stress | Source manuscript supports left=100/right=0; verify against app/logging code |
| `understanding` | Self-reported ease of understanding | 0-1000 | 0-100 | Greater perceived understanding | Source manuscript supports left=100/right=0; exact anchors still needed |
| `memorability` | Perceived memorability | 0-1000 | 0-100 | Greater perceived memorability | Source manuscript supports left=100/right=0; exact anchors still needed |

## Stress Coding Risk

The static UI example in `src/sample_ui_en.html` shows the stress slider with the left anchor "Unbearable stress" and the right anchor "No stress at all". The Japanese source manuscript states that VAS responses used left=100 and right=0. If the original experimental application used this coding, higher stress values mean greater stress and the current stress interpretation is directionally consistent. This should still be verified from the original Unity project or raw export documentation before the stress result is treated as fully resolved.

## Submission Requirement

Before journal submission, add a table to the manuscript with:

- exact item wording
- left and right anchors
- raw scale range
- normalized scale range
- default slider position
- scoring direction
- reverse-coding procedure, if used
