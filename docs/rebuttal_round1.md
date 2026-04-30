# Response to Reviewers, Round 1

We thank the editor and reviewers for their detailed and constructive comments. We agree that the original manuscript overstated several claims and was not yet prepared as a CHBR-compliant double-anonymized submission. We have substantially revised the manuscript, analysis pipeline, and submission package. The revised manuscript is now framed as an exploratory study of streamed versus full-text presentation, with claims limited to self-reported user experience and task completion time.

## Response to the Handling Editor

**Comment: The manuscript was not prepared for double-anonymized review and lacked required submission materials.**

Response: We agree. We removed author names, affiliations, corresponding-author information, and author footnotes from the main manuscript. We prepared a separate title page file containing author information. We also added separate highlights and declaration files.

Changes made:

- Main anonymized manuscript: `paper/main.tex`
- Separate title page: `paper/title_page.tex`
- Highlights: `paper/highlights.md`
- Declarations placeholder: `paper/declarations.md`

**Comment: Human-subject ethics reporting is incomplete.**

Response: We agree. We have not invented ethics information that is not yet confirmed. Instead, we added a dedicated declarations file and revision plan identifying ethics approval or waiver details as a blocking item before CHBR submission. The final manuscript will require the approving body or waiver authority, date, reference number, consent procedure, privacy protection procedure, and handling of participants aged 16-17.

Changes made:

- `paper/declarations.md`
- `docs/chbr_revision_plan.md`
- `docs/publication_checklist.md`

**Comment: The empirical contribution and claims were too strong for the evidence.**

Response: We agree. We revised the title, abstract, discussion, and conclusion to frame the study as exploratory. We removed or weakened claims about objective comprehension, deeper processing, learning benefits, and design guidelines. The revised claim is that character-by-character presentation was associated with longer task completion time and unadjusted differences in self-reported ease of understanding and stress, while only completion time remained significant after Holm correction.

## Response to Reviewer 1: HCI and Usability

**Comment 1: "Understanding" is subjective, but the paper claims comprehension or deeper processing.**

Response: We agree. The original wording overstated the construct. We revised the manuscript throughout to refer to this outcome as "self-reported ease of understanding" or "perceived understanding." We removed claims about objective comprehension, comprehension depth, and learning benefits. We also added an explicit limitation stating that no objective comprehension, recall, transfer, or delayed retention measure was administered.

Changes made:

- Abstract revised.
- Measurement framework revised.
- Results and Discussion revised.
- Limitations revised.
- Conclusion revised.

**Comment 2: Reading time is confounded with the forced display rate.**

Response: We agree. We reframed the time variable as "task completion time under display constraints" rather than reading speed or reading efficiency. We now state that the character-by-character condition mechanically constrained the earliest possible completion point and that the time result should not be interpreted as pure reading efficiency.

Changes made:

- Measurement Framework
- Procedure
- Statistical Analysis Results
- Conclusion

**Comment 3: Ecological validity is limited by use of a single literary excerpt.**

Response: We agree. We revised the manuscript to describe the study as a single-stimulus exploratory study. We added a source document for the stimulus and cited the Aozora Bunko source in the manuscript. We also removed broad claims about web systems generally and added the need for multi-text replication as a limitation.

Changes made:

- `docs/stimulus_source.md`
- `paper/refworks.bib`
- Materials and Apparatus
- Limitations and Future Directions

**Comment 4: The HCI contribution is not yet strong enough for broad design guidance.**

Response: We agree. We reframed the paper around streamed text presentation, progressive disclosure, perceived understanding, affective response, and completion time. We removed language implying final design guidelines and now present the results as preliminary evidence that should motivate larger, better-controlled studies.

## Response to Reviewer 2: Behavioral Methods and Statistics

**Comment 1: Potential reverse-coding problem in the stress VAS.**

Response: We investigated this issue using the original Japanese manuscript and author-provided item wording. The original questionnaire documentation states that the left endpoint was coded as 100 and the right endpoint as 0. The stress item used the left anchor "Unbearable stress" and the right anchor "No stress at all." Therefore, higher normalized stress values indicate greater stress, and no reverse coding is required. We added a VAS codebook documenting all item wordings, anchors, scale ranges, and scoring directions.

Changes made:

- `docs/vas_codebook.md`
- Visual Analog Scale Implementation
- Statistical Significance Summary
- Discussion
- Conclusion

**Comment 2: Sample size and power analysis are incorrect or underreported.**

Response: We agree. We corrected the power statement. The manuscript now states that the original claim of 80% power for d = 0.8 with n = 12 per group is not statistically defensible. We added a sensitivity power analysis showing that the design has approximately 47% power for d = 0.8 and that approximately d = 1.20 is required for 80% power. We now treat the study as exploratory.

Changes made:

- Participants section
- `src/study_analysis.py`
- `src/analyze_data.py`
- `docs/analysis_results.md`

**Comment 3: Multiple testing was not controlled, and confidence intervals and robustness checks were missing.**

Response: We agree. We expanded the analysis pipeline. The revised analysis reports Welch's independent-samples t-tests for all outcomes, mean differences, 95% confidence intervals, Hedges' g, bootstrap confidence intervals for Hedges' g, Holm-adjusted p-values, Bonferroni-adjusted p-values, Benjamini-Hochberg adjusted p-values, Mann-Whitney U tests, permutation tests, Shapiro-Wilk checks, and Levene tests. The manuscript now emphasizes that only completion time remains significant after Holm correction.

Changes made:

- `src/study_analysis.py`
- `src/analyze_data.py`
- `docs/analysis_results.md`
- Inferential Statistics
- Statistical Significance Summary

**Comment 4: VAS design, anchors, scaling, and interpretation were underreported.**

Response: We agree. We documented the exact item wording and left/right anchors for all four VAS items. The original questionnaire used left=100 and right=0, and the raw application values were normalized from 0-1000 to 0-100. Higher values therefore indicate greater readability, greater stress, greater self-reported ease of understanding, and greater perceived memorability.

Changes made:

- `docs/vas_codebook.md`
- Visual Analog Scale Implementation

**Comment 5: Stimulus and rate details are internally inconsistent or underreported.**

Response: We partially addressed this issue. We documented the stimulus source and cited the Aozora Bunko version of Akutagawa's "Hana" ("The Nose"). We also clarified that the 0.1 s/character rate equals 10 characters per second and should be interpreted as an implementation choice, not a direct replication of the approximately 6 letters/second optimum reported in prior work. Exact stimulus length, line breaks, font, and display layout still need to be documented from the original experimental materials before submission.

Changes made:

- `docs/stimulus_source.md`
- Materials and Apparatus
- `paper/refworks.bib`

## Response to Minor Comments

**Title**

Response: We revised the title to narrow the scope and avoid implying a broad taxonomy of text output methods.

New title:

"Streaming Versus Full-Text Presentation in Web Interfaces: Effects on Perceived Understanding, Stress, and Completion Time"

**Abstract**

Response: We revised the abstract to use "self-reported ease of understanding," "task completion time," and "exploratory study." We removed "fundamental trade-off" and objective comprehension language.

**Keywords**

Response: We reduced the keyword list to seven keywords.

**Highlights**

Response: We added a separate highlights file with four concise highlights.

**Section structure**

Response: We renamed "Results and Discussion" to "Discussion" and reduced repeated statistical interpretation.

**Reference style and citation mismatches**

Response: We changed the bibliography style from numbered `unsrt` to `apalike` and corrected author-name mismatches for Darejeh et al. and Amadieu et al.

**Author footnotes**

Response: We removed placeholder author footnotes from the anonymized manuscript.

**Copyright/source**

Response: We added source metadata for Akutagawa's "Hana" from Aozora Bunko and cited it in the manuscript.

## Remaining Items Before Submission

The following items still require author confirmation or additional source material before CHBR submission:

- Ethics approval or waiver details.
- Exact stimulus length, line breaks, font, and display layout.
- Participant recruitment source, compensation, demographics, language/reading background, randomization procedure, and group balance.
- Funding statement.
- Competing-interest declaration.
- CRediT author statement.
- Generative AI declaration, if applicable.

We have documented these remaining blockers in `docs/chbr_revision_plan.md` and `docs/publication_checklist.md`.
