#!/usr/bin/env python3
"""Shared analysis utilities for the text presentation study."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


MEASURES = ["readability", "stress", "understanding", "memorability", "time"]
SUBJECTIVE_MEASURES = ["readability", "stress", "understanding", "memorability"]
GROUPS = ["A", "B"]
GROUP_LABELS = {
    "A": "Group A (Character-by-character)",
    "B": "Group B (Full text)",
}
MEASURE_LABELS = {
    "readability": "Readability",
    "stress": "Stress",
    "understanding": "Understanding",
    "memorability": "Memorability",
    "time": "Time (seconds)",
}


@dataclass(frozen=True)
class TestResult:
    measure: str
    levene_statistic: float
    levene_p_value: float
    equal_variance_assumed: bool
    test_name: str
    degrees_of_freedom: float
    t_statistic: float
    p_value: float
    cohen_d: float

    @property
    def significant(self) -> bool:
        return self.p_value < 0.05

    @property
    def variance_homogeneity(self) -> str:
        return "Homogeneous" if self.equal_variance_assumed else "Not homogeneous"


def default_data_path() -> Path:
    return Path(__file__).with_name("data_all.csv")


def load_dataset(path: Path | str = default_data_path()) -> pd.DataFrame:
    """Load and validate the anonymized study dataset."""
    data = pd.read_csv(path)
    expected_columns = ["group", *MEASURES]
    missing_columns = [column for column in expected_columns if column not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    data = data[expected_columns].copy()
    unexpected_groups = sorted(set(data["group"]) - set(GROUPS))
    if unexpected_groups:
        raise ValueError(f"Unexpected group labels: {unexpected_groups}")

    if data[expected_columns].isna().any().any():
        raise ValueError("Dataset contains missing values")

    for measure in MEASURES:
        data[measure] = pd.to_numeric(data[measure], errors="raise")

    group_counts = data["group"].value_counts().to_dict()
    if any(group_counts.get(group, 0) == 0 for group in GROUPS):
        raise ValueError(f"Both groups must be present: {GROUPS}")

    return data


def descriptive_statistics(data: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Return min, median, mean, max, and sample SD for each group."""
    summaries: dict[str, pd.DataFrame] = {}
    for group in GROUPS:
        group_data = data[data["group"] == group][MEASURES]
        summaries[group] = group_data.agg(["min", "median", "mean", "max", "std"]).T
    return summaries


def run_group_tests(data: pd.DataFrame, alpha: float = 0.05) -> list[TestResult]:
    """Run Levene tests and independent-samples t-tests for all measures."""
    results = []
    for measure in MEASURES:
        group_a = data.loc[data["group"] == "A", measure].to_numpy()
        group_b = data.loc[data["group"] == "B", measure].to_numpy()

        levene = stats.levene(group_a, group_b, center="mean")
        equal_variance = bool(levene.pvalue >= alpha)
        t_test = stats.ttest_ind(group_a, group_b, equal_var=equal_variance)
        df = _degrees_of_freedom(group_a, group_b, equal_variance)

        results.append(
            TestResult(
                measure=measure,
                levene_statistic=float(levene.statistic),
                levene_p_value=float(levene.pvalue),
                equal_variance_assumed=equal_variance,
                test_name="Student t-test" if equal_variance else "Welch t-test",
                degrees_of_freedom=float(df),
                t_statistic=float(t_test.statistic),
                p_value=float(t_test.pvalue),
                cohen_d=float(_cohen_d(group_a, group_b)),
            )
        )
    return results


def tests_to_frame(results: list[TestResult]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "measure": result.measure,
                "variance_homogeneity": result.variance_homogeneity,
                "levene_p_value": result.levene_p_value,
                "test": result.test_name,
                "df": result.degrees_of_freedom,
                "t": result.t_statistic,
                "p_value": result.p_value,
                "cohen_d": result.cohen_d,
                "significant": result.significant,
            }
            for result in results
        ]
    )


def _degrees_of_freedom(group_a: np.ndarray, group_b: np.ndarray, equal_variance: bool) -> float:
    if equal_variance:
        return len(group_a) + len(group_b) - 2

    var_a = np.var(group_a, ddof=1)
    var_b = np.var(group_b, ddof=1)
    n_a = len(group_a)
    n_b = len(group_b)
    numerator = (var_a / n_a + var_b / n_b) ** 2
    denominator = ((var_a / n_a) ** 2 / (n_a - 1)) + ((var_b / n_b) ** 2 / (n_b - 1))
    return numerator / denominator


def _cohen_d(group_a: np.ndarray, group_b: np.ndarray) -> float:
    n_a = len(group_a)
    n_b = len(group_b)
    pooled_variance = (
        ((n_a - 1) * np.var(group_a, ddof=1) + (n_b - 1) * np.var(group_b, ddof=1))
        / (n_a + n_b - 2)
    )
    return (np.mean(group_a) - np.mean(group_b)) / np.sqrt(pooled_variance)
