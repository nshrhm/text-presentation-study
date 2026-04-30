# Data Dictionary

This document describes `src/data_all.csv`, the anonymized participant-level dataset used for the manuscript figures.

## File

`src/data_all.csv`

## Unit of Observation

Each row represents one participant. The dataset contains 24 rows: 12 participants in Group A and 12 participants in Group B.

## Variables

| Column | Type | Description |
| --- | --- | --- |
| `group` | Categorical | Experimental condition. `A` indicates character-by-character text presentation. `B` indicates immediate full-text presentation. |
| `readability` | Numeric | Visual Analog Scale rating for perceived readability. Values are normalized to a 0-100 scale. |
| `stress` | Numeric | Visual Analog Scale rating for perceived stress. Values are normalized to a 0-100 scale. |
| `understanding` | Numeric | Visual Analog Scale rating for perceived ease of understanding. Values are normalized to a 0-100 scale. |
| `memorability` | Numeric | Visual Analog Scale rating for perceived memorability. Values are normalized to a 0-100 scale. |
| `time` | Numeric | Reading time in seconds. |

## Condition Coding

Group A used character-by-character presentation at a fixed presentation rate. Group B saw the full text immediately.

## Missing Data

The current public dataset contains no missing values.

## Privacy Notes

The dataset does not include participant names, contact information, device identifiers, IP addresses, or free-text responses. Rows should not be treated as personally identifying records.
