"""Chronological partitions; test targets are never evaluated in Week 1."""

import pandas as pd

WINDOWS = {
    "train": ("2011-01-01", "2011-12-31"),
    "validation": ("2012-01-01", "2012-06-30"),
    "test": ("2012-07-01", "2012-12-31"),
}


def split_data(frame: pd.DataFrame) -> dict[str, pd.DataFrame]:
    if frame.empty:
        raise ValueError("Cannot split an empty dataset")

    if "dteday" not in frame.columns:
        raise ValueError("Missing dteday column")

    dates = pd.to_datetime(frame["dteday"], errors="raise")

    if dates.isna().any():
        raise ValueError("dteday: missing dates")

    partitions = {}

    for name, (start, end) in WINDOWS.items():
        mask = dates.between(pd.Timestamp(start), pd.Timestamp(end))

        part = frame.loc[mask].copy()
        part = part.sort_values(
            by=["dteday", "hr"] if "hr" in part.columns else ["dteday"],
            kind="stable",
        )

        if part.empty:
            raise ValueError(f"{name}: partition must be nonempty")

        partitions[name] = part

    all_indices = [index for part in partitions.values() for index in part.index]

    if len(all_indices) != len(frame):
        raise ValueError("Partitions must provide complete coverage of input rows")

    if len(set(all_indices)) != len(all_indices):
        raise ValueError("Partitions overlap")

    return partitions


def partition_summary(partitions: dict[str, pd.DataFrame]) -> dict:
    return {
        name: {
            "rows": len(part),
            "date_min": str(part["dteday"].min().date()),
            "date_max": str(part["dteday"].max().date()),
        }
        for name, part in partitions.items()
    }
