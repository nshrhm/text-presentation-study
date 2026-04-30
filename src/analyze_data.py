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

    args.output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = args.output_dir / "analysis_results.md"
    json_path = args.output_dir / "analysis_results.json"

    markdown_path.write_text(
        build_markdown(
            data_path=_display_path(data_path, repo_root),
            summaries=summaries,
            test_frame=test_frame,
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
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {markdown_path}")
    print(f"Wrote {json_path}")


def build_markdown(data_path: str, summaries, test_frame) -> str:
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
            "Levene's test uses mean-centered variance comparison. Independent-samples t-tests use equal variances when Levene's test is not significant at alpha = 0.05.",
            "",
            _test_table(test_frame),
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
    header = "| Measure | Variance | Test | df | t | p | Cohen's d |"
    separator = "| --- | --- | --- | ---: | ---: | ---: | ---: |"
    rows = [header, separator]
    for _, row in test_frame.iterrows():
        rows.append(
            "| {label} | {variance} | {test} | {df:.2f} | {t:.2f} | {p:.4f} | {d:.2f} |".format(
                label=MEASURE_LABELS[row["measure"]],
                variance=row["variance_homogeneity"],
                test=row["test"],
                df=row["df"],
                t=row["t"],
                p=row["p_value"],
                d=row["cohen_d"],
            )
        )
    return "\n".join(rows)


if __name__ == "__main__":
    main()
