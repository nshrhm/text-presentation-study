#!/usr/bin/env python3
"""Generate reviewer-facing statistical analysis outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from study_analysis import (
    GROUP_LABELS,
    MEASURE_LABELS,
    descriptive_statistics,
    load_dataset,
    run_group_tests,
    sensitivity_power_analysis,
    tests_to_frame,
)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description="Regenerate statistical analysis results")
    parser.add_argument("--data", type=Path, default=Path(__file__).with_name("data_all.csv"))
    parser.add_argument("--output-dir", type=Path, default=repo_root / "docs")
    args = parser.parse_args()

    data_path = args.data.resolve()
    data = load_dataset(data_path)
    summaries = descriptive_statistics(data)
    tests = run_group_tests(data)
    test_frame = tests_to_frame(tests)
    power = sensitivity_power_analysis(n_per_group=12)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = args.output_dir / "analysis_results.md"
    json_path = args.output_dir / "analysis_results.json"

    markdown_path.write_text(
        build_markdown(
            data_path=_display_path(data_path, repo_root),
            summaries=summaries,
            test_frame=test_frame,
            power=power,
        ),
        encoding="utf-8",
    )
    json_path.write_text(
        json.dumps(
            {
                "data": _display_path(data_path, repo_root),
                "descriptive_statistics": {
                    group: summary.reset_index(names="measure").to_dict(orient="records")
                    for group, summary in summaries.items()
                },
                "tests": test_frame.to_dict(orient="records"),
                "sensitivity_power_analysis": power,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {markdown_path}")
    print(f"Wrote {json_path}")


def build_markdown(data_path: str, summaries, test_frame, power: dict[str, float]) -> str:
    lines = [
        "# Analysis Results",
        "",
        "This file is generated from `src/data_all.csv` by `src/analyze_data.py`.",
        "",
        f"Input dataset: `{data_path}`",
        "",
        "## Descriptive Statistics",
        "",
    ]

    for group, summary in summaries.items():
        lines.extend(
            [
                f"### {GROUP_LABELS[group]}",
                "",
                _summary_table(summary),
                "",
            ]
        )

    lines.extend(
        [
            "## Inferential Statistics",
            "",
            "All inferential tests are exploratory. Welch's independent-samples t-tests are reported as the primary parametric comparison for robustness to unequal variances. Holm-adjusted p-values control the family-wise error rate across the five outcomes.",
            "",
            _test_table(test_frame),
            "",
            "## Robustness and Assumption Checks",
            "",
            _robustness_table(test_frame),
            "",
            "## Sensitivity Power Analysis",
            "",
            f"With 12 participants per group and alpha = {power['alpha']:.2f}, the design has estimated power of {power['power_for_d_0_8']:.2f} for Cohen's d = 0.8 in a two-sided independent-samples t-test.",
            f"The estimated standardized mean difference required for 80% power is d = {power['d_for_80_percent_power']:.2f}.",
            "",
        ]
    )
    return "\n".join(lines)


def _display_path(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def _summary_table(summary) -> str:
    header = "| Measure | Minimum | Median | Mean | Maximum | SD |"
    separator = "| --- | ---: | ---: | ---: | ---: | ---: |"
    rows = [header, separator]
    for measure, row in summary.iterrows():
        rows.append(
            "| {label} | {min:.2f} | {median:.2f} | {mean:.2f} | {max:.2f} | {std:.2f} |".format(
                label=MEASURE_LABELS[measure],
                min=row["min"],
                median=row["median"],
                mean=row["mean"],
                max=row["max"],
                std=row["std"],
            )
        )
    return "\n".join(rows)


def _test_table(test_frame) -> str:
    header = "| Measure | Mean A | Mean B | A-B | 95% CI | Welch p | Holm p | Hedges g | g 95% CI |"
    separator = "| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |"
    rows = [header, separator]
    for _, row in test_frame.iterrows():
        rows.append(
            "| {label} | {mean_a:.2f} | {mean_b:.2f} | {diff:.2f} | [{ci_low:.2f}, {ci_high:.2f}] | {p:.4f} | {holm:.4f} | {g:.2f} | [{g_low:.2f}, {g_high:.2f}] |".format(
                label=MEASURE_LABELS[row["measure"]],
                mean_a=row["mean_a"],
                mean_b=row["mean_b"],
                diff=row["mean_difference"],
                ci_low=row["mean_difference_ci_low"],
                ci_high=row["mean_difference_ci_high"],
                p=row["p_value"],
                holm=row["holm_p_value"],
                g=row["hedges_g"],
                g_low=row["hedges_g_ci_low"],
                g_high=row["hedges_g_ci_high"],
            )
        )
    return "\n".join(rows)


def _robustness_table(test_frame) -> str:
    header = "| Measure | Levene p | Shapiro A p | Shapiro B p | Mann-Whitney p | Permutation p | BH p |"
    separator = "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"
    rows = [header, separator]
    for _, row in test_frame.iterrows():
        rows.append(
            "| {label} | {levene:.4f} | {shapiro_a:.4f} | {shapiro_b:.4f} | {mw:.4f} | {perm:.4f} | {bh:.4f} |".format(
                label=MEASURE_LABELS[row["measure"]],
                levene=row["levene_p_value"],
                shapiro_a=row["shapiro_p_value_a"],
                shapiro_b=row["shapiro_p_value_b"],
                mw=row["mann_whitney_p_value"],
                perm=row["permutation_p_value"],
                bh=row["benjamini_hochberg_p_value"],
            )
        )
    return "\n".join(rows)


if __name__ == "__main__":
    main()
