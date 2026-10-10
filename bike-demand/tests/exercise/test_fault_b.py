"""Personal Fault B: reject a negative rental count."""

import pandas as pd
import pytest

from bike_demand.validate import load_data


@pytest.mark.exercise
def test_fault_b_negative_count(tmp_path):
    # Start from a valid, small copy of the training data.
    frame = pd.read_csv("data/raw/hour.csv").query("yr == 0").head(5).copy()

    # Valid control: the original rows must pass validation.
    control = tmp_path / "control.csv"
    frame.to_csv(control, index=False)
    assert len(load_data(control)) == 5

    # Fault B: change only one value, without removing columns.
    frame.loc[frame.index[0], "cnt"] = -1
    faulty = tmp_path / "fault-b-negative-count.csv"
    frame.to_csv(faulty, index=False)

    # The validator must reject the specific broken rule.
    with pytest.raises(ValueError, match="cnt: counts must be non-negative integers"):
        load_data(faulty)
