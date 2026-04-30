# VAS Codebook

This codebook records the information needed to interpret the Visual Analog Scale variables in `src/data_all.csv`.

## Current Status

The public CSV contains normalized 0-100 values for the following variables:

- `readability`
- `stress`
- `understanding`
- `memorability`

The item wording and anchors have been confirmed by the author. The Japanese source manuscript `original.pdf` states that participants answered by moving a slider where the left endpoint was 100 and the right endpoint was 0. Therefore, all four public VAS variables are coded so that higher values indicate more of the named construct.

## Required Item-Level Documentation

| Variable | Item wording | Left anchor | Right anchor | Raw scale | Normalized scale | Higher values mean |
| --- | --- | --- | --- | --- | --- | --- |
| `readability` | Was it easy to read? | Easier to read than anything experienced before | The highest possible difficulty reading | 0-1000 | 0-100 | More readable |
| `stress` | Did you feel stress? | Unbearable stress | No stress at all | 0-1000 | 0-100 | More stress |
| `understanding` | Was the text easy to understand? | Completely understood | Could not understand at all | 0-1000 | 0-100 | Greater self-reported ease of understanding |
| `memorability` | Was the content easy to remember? | Completely remembered | Could not remember at all | 0-1000 | 0-100 | Greater perceived memorability |

## Stress Coding Risk

The stress item used the left anchor "Unbearable stress" and the right anchor "No stress at all." Because the source manuscript states left=100 and right=0, higher normalized stress values indicate greater stress. The stress interpretation in the analysis is therefore directionally consistent with the instrument documentation.

## Submission Requirement

Before journal submission, add a table to the manuscript with:

- exact item wording
- left and right anchors
- raw scale range
- normalized scale range
- default slider position, if available
- scoring direction
- reverse-coding procedure, if used; based on current documentation, no reverse coding is required
