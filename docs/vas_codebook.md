# VAS Codebook

This codebook records the information needed to interpret the Visual Analog Scale variables in `src/data_all.csv`.

## Current Status

The public CSV contains normalized 0-100 values for the following variables:

- `readability`
- `stress`
- `understanding`
- `memorability`

The item wording and anchors have been confirmed by the author. The Japanese source manuscript `original.pdf`, archived outside the public repository, states that participants answered by moving a slider where the left endpoint was 100 and the right endpoint was 0. Therefore, all four public VAS variables are coded so that higher values indicate more of the named construct.

## Required Item-Level Documentation

| Variable | Item wording | Left anchor | Right anchor | Raw scale | Normalized scale | Higher values mean |
| --- | --- | --- | --- | --- | --- | --- |
| `readability` | Was it easy to read? | Easier to read than anything experienced before | The highest possible difficulty reading | 0-1000 | 0-100 | More readable |
| `stress` | Did you feel stress? | Unbearable stress | No stress at all | 0-1000 | 0-100 | More stress |
| `understanding` | Was the text easy to understand? | Completely understood | Could not understand at all | 0-1000 | 0-100 | Greater self-reported ease of understanding |
| `memorability` | Was the content easy to remember? | Completely remembered | Could not remember at all | 0-1000 | 0-100 | Greater perceived memorability |

## Stress Coding Risk

The stress item used the left anchor "Unbearable stress" and the right anchor "No stress at all." Because the source manuscript states left=100 and right=0, higher normalized stress values indicate greater stress. The stress interpretation in the analysis is therefore directionally consistent with the instrument documentation.

## Remaining Reporting Limitations

The manuscript now includes a VAS codebook table. Remaining details that should be recovered from the original UI materials if possible:

- default slider position, if available
- any UI constraint that prevented submission without moving the slider
- screenshots or source UI files that independently document the item order and default state

Based on current documentation, no reverse coding is required.
