# Experimental Plan

This document summarizes the study design for reviewers. The manuscript remains the authoritative source for the final reported analysis and interpretation.

## Objective

The study evaluates how text presentation method affects user experience in a web-interface reading task. The comparison focuses on character-by-character display versus immediate full-text display.

## Research Question

Does character-by-character text presentation differ from full-text presentation in subjective usability ratings and reading time?

## Design

The study used a between-subjects experimental design with two conditions:

- Group A: character-by-character text presentation
- Group B: full-text presentation

The between-subjects design was selected to avoid carryover effects that could occur if participants experienced both presentation methods.

## Participants

The study included 24 adult participants with web service experience. Participants were assigned to one of the two conditions, resulting in 12 participants per group.

## Task

Participants read the same text stimulus and then completed subjective evaluations using Visual Analog Scale items. Reading time was recorded during the reading phase.

## Measures

The subjective measures were:

- readability
- stress
- understanding
- memorability

The objective measure was:

- reading time in seconds

## Analysis Overview

The analysis compared Group A and Group B across all five measures. Mean-centered Levene tests were used to evaluate variance homogeneity before selecting the appropriate t-test procedure. The current public analysis uses Student independent-samples t-tests for all five measures because Levene's tests were not significant at alpha = 0.05. The manuscript reports p-values and interprets the results with respect to usability and reading-performance trade-offs.

## Reviewer Notes

The public repository includes the anonymized CSV dataset, statistical analysis script, figure-generation script, regenerated analysis outputs, and rebuilt PDF. It does not include private development notes, informal drafts, or any content from `backup/`.
