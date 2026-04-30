#!/usr/bin/env python3
"""Shared analysis utilities for the text presentation study."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq
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
    mean_a: float
    mean_b: float
    mean_difference: float
    mean_difference_ci_low: float
    mean_difference_ci_high: float
    levene_p_value: float
    test_name: str
    degrees_of_freedom: float
    t_statistic: float
    p_value: float
    holm_p_value: float
    bonferroni_p_value: float
    benjamini_hochberg_p_value: float
    hedges_g: float
    hedges_g_ci_low: float
    hedges_g_ci_high: float
    mann_whitney_p_value: float
    permutation_p_value: float
    shapiro_p_value_a: float
    shapiro_p_value_b: float

    @property
    def significant(self) -> bool:
        return self.p_value < 0.05

    @property
    def variance_homogeneity(self) -> str:
        return "Homogeneous" if self.levene_p_value >= 0.05 else "Not homogeneous"


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
    """Run exploratory Welch tests and robustness checks for all measures."""
    raw_results = []
    for measure in MEASURES:
        group_a = data.loc[data["group"] == "A", measure].to_numpy()
        group_b = data.loc[data["group"] == "B", measure].to_numpy()

        levene = stats.levene(group_a, group_b, center="mean")
        t_test = stats.ttest_ind(group_a, group_b, equal_var=False)
        df = _welch_degrees_of_freedom(group_a, group_b)
        mean_difference = float(np.mean(group_a) - np.mean(group_b))
        ci_low, ci_high = _mean_difference_ci(group_a, group_b, alpha)
        hedges_g = _hedges_g(group_a, group_b)
        g_ci_low, g_ci_high = _bootstrap_hedges_g_ci(group_a, group_b, measure)
        mann_whitney = stats.mannwhitneyu(group_a, group_b, alternative="two-sided")
        permutation = stats.permutation_test(
            (group_a, group_b),
            _mean_difference_statistic,
            alternative="two-sided",
            permutation_type="independent",
            n_resamples=50000,
            random_state=np.random.default_rng(_seed_for_measure(measure)),
        )
        shapiro_a = stats.shapiro(group_a)
        shapiro_b = stats.shapiro(group_b)

        raw_results.append(
            {
                "measure": measure,
                "mean_a": float(np.mean(group_a)),
                "mean_b": float(np.mean(group_b)),
                "mean_difference": mean_difference,
                "mean_difference_ci_low": ci_low,
                "mean_difference_ci_high": ci_high,
                "levene_p_value": float(levene.pvalue),
                "test_name": "Welch t-test",
                "degrees_of_freedom": float(df),
                "t_statistic": float(t_test.statistic),
                "p_value": float(t_test.pvalue),
                "hedges_g": float(hedges_g),
                "hedges_g_ci_low": float(g_ci_low),
                "hedges_g_ci_high": float(g_ci_high),
                "mann_whitney_p_value": float(mann_whitney.pvalue),
                "permutation_p_value": float(permutation.pvalue),
                "shapiro_p_value_a": float(shapiro_a.pvalue),
                "shapiro_p_value_b": float(shapiro_b.pvalue),
            }
        )

    p_values = [result["p_value"] for result in raw_results]
    holm = _holm_adjusted_p_values(p_values)
    bonferroni = [min(p_value * len(p_values), 1.0) for p_value in p_values]
    bh = _benjamini_hochberg_adjusted_p_values(p_values)

    results = []
    for result, holm_p, bonferroni_p, bh_p in zip(raw_results, holm, bonferroni, bh):
        results.append(
            TestResult(
                **result,
                holm_p_value=float(holm_p),
                bonferroni_p_value=float(bonferroni_p),
                benjamini_hochberg_p_value=float(bh_p),
            )
        )
    return results


def tests_to_frame(results: list[TestResult]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "measure": result.measure,
                "mean_a": result.mean_a,
                "mean_b": result.mean_b,
                "mean_difference": result.mean_difference,
                "mean_difference_ci_low": result.mean_difference_ci_low,
                "mean_difference_ci_high": result.mean_difference_ci_high,
                "variance_homogeneity": result.variance_homogeneity,
                "levene_p_value": result.levene_p_value,
                "test": result.test_name,
                "df": result.degrees_of_freedom,
                "t": result.t_statistic,
                "p_value": result.p_value,
                "holm_p_value": result.holm_p_value,
                "bonferroni_p_value": result.bonferroni_p_value,
                "benjamini_hochberg_p_value": result.benjamini_hochberg_p_value,
                "hedges_g": result.hedges_g,
                "hedges_g_ci_low": result.hedges_g_ci_low,
                "hedges_g_ci_high": result.hedges_g_ci_high,
                "mann_whitney_p_value": result.mann_whitney_p_value,
                "permutation_p_value": result.permutation_p_value,
                "shapiro_p_value_a": result.shapiro_p_value_a,
                "shapiro_p_value_b": result.shapiro_p_value_b,
                "significant": result.significant,
            }
            for result in results
        ]
    )


def sensitivity_power_analysis(n_per_group: int = 12, alpha: float = 0.05) -> dict[str, float]:
    """Return power for d=0.8 and detectable d for 80% power."""
    return {
        "n_per_group": float(n_per_group),
        "alpha": float(alpha),
        "power_for_d_0_8": float(_two_sample_t_power(0.8, n_per_group, n_per_group, alpha)),
        "d_for_80_percent_power": float(
            brentq(lambda d: _two_sample_t_power(d, n_per_group, n_per_group, alpha) - 0.8, 0.01, 5.0)
        ),
    }


def _welch_degrees_of_freedom(group_a: np.ndarray, group_b: np.ndarray) -> float:
    var_a = np.var(group_a, ddof=1)
    var_b = np.var(group_b, ddof=1)
    n_a = len(group_a)
    n_b = len(group_b)
    numerator = (var_a / n_a + var_b / n_b) ** 2
    denominator = ((var_a / n_a) ** 2 / (n_a - 1)) + ((var_b / n_b) ** 2 / (n_b - 1))
    return numerator / denominator


def _mean_difference_ci(group_a: np.ndarray, group_b: np.ndarray, alpha: float) -> tuple[float, float]:
    mean_difference = np.mean(group_a) - np.mean(group_b)
    standard_error = np.sqrt(np.var(group_a, ddof=1) / len(group_a) + np.var(group_b, ddof=1) / len(group_b))
    df = _welch_degrees_of_freedom(group_a, group_b)
    critical = stats.t.ppf(1 - alpha / 2, df)
    return float(mean_difference - critical * standard_error), float(mean_difference + critical * standard_error)


def _hedges_g(group_a: np.ndarray, group_b: np.ndarray) -> float:
    return _cohen_d(group_a, group_b) * _hedges_correction(len(group_a), len(group_b))


def _cohen_d(group_a: np.ndarray, group_b: np.ndarray) -> float:
    n_a = len(group_a)
    n_b = len(group_b)
    pooled_variance = (
        ((n_a - 1) * np.var(group_a, ddof=1) + (n_b - 1) * np.var(group_b, ddof=1))
        / (n_a + n_b - 2)
    )
    return (np.mean(group_a) - np.mean(group_b)) / np.sqrt(pooled_variance)


def _hedges_correction(n_a: int, n_b: int) -> float:
    df = n_a + n_b - 2
    return 1 - (3 / (4 * df - 1))


def _bootstrap_hedges_g_ci(group_a: np.ndarray, group_b: np.ndarray, measure: str) -> tuple[float, float]:
    rng = np.random.default_rng(_seed_for_measure(measure) + 1000)
    values = []
    for _ in range(10000):
        sample_a = rng.choice(group_a, size=len(group_a), replace=True)
        sample_b = rng.choice(group_b, size=len(group_b), replace=True)
        if np.std(sample_a, ddof=1) == 0 and np.std(sample_b, ddof=1) == 0:
            continue
        values.append(_hedges_g(sample_a, sample_b))
    return tuple(float(value) for value in np.percentile(values, [2.5, 97.5]))


def _mean_difference_statistic(group_a: np.ndarray, group_b: np.ndarray, axis: int = 0) -> np.ndarray:
    return np.mean(group_a, axis=axis) - np.mean(group_b, axis=axis)


def _holm_adjusted_p_values(p_values: list[float]) -> list[float]:
    count = len(p_values)
    order = np.argsort(p_values)
    adjusted = np.empty(count)
    running_max = 0.0
    for rank, index in enumerate(order):
        candidate = min((count - rank) * p_values[index], 1.0)
        running_max = max(running_max, candidate)
        adjusted[index] = running_max
    return adjusted.tolist()


def _benjamini_hochberg_adjusted_p_values(p_values: list[float]) -> list[float]:
    count = len(p_values)
    order = np.argsort(p_values)[::-1]
    adjusted = np.empty(count)
    running_min = 1.0
    for rank_from_end, index in enumerate(order):
        rank = count - rank_from_end
        candidate = min(p_values[index] * count / rank, 1.0)
        running_min = min(running_min, candidate)
        adjusted[index] = running_min
    return adjusted.tolist()


def _two_sample_t_power(effect_size_d: float, n_a: int, n_b: int, alpha: float) -> float:
    df = n_a + n_b - 2
    noncentrality = effect_size_d / np.sqrt(1 / n_a + 1 / n_b)
    critical = stats.t.ppf(1 - alpha / 2, df)
    return stats.nct.sf(critical, df, noncentrality) + stats.nct.cdf(-critical, df, noncentrality)


def _seed_for_measure(measure: str) -> int:
    return 20260430 + sum(ord(char) for char in measure)
