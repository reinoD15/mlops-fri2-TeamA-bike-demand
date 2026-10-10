# mlops-fri2-TeamA-bike-demand

# Bike Demand Prediction (MLOps)

This repository contains the source code for the MLOps learning project (Week 1, Lab 2) focused on predicting bike demand (using the `hour.csv` dataset). The project implements a complete pipeline including strict data validation, chronological partitioning, model training (Random Forest vs. Naive Baseline), and experiment tracking with MLflow.

## Prerequisites

To run this project, you need the following:

* **Python**: Version `3.12` strictly.
* **Package Manager**: [uv](https://github.com/astral-sh/uv) for fast and deterministic dependency resolution.

## Installation

1. Clone this repository.
2. Ensure you are using Python 3.12.
3. Install dependencies and create the virtual environment from the lock file:

   ```bash
   uv sync --locked
   ```

## Project Structure

The minimal architecture expected by the preflight verification pipeline is as follows:

```text
├── configs/
│   └── baseline.yaml       # Training configuration (features, hyperparameters)
├── data/
│   ├── manifest.json       # Checksums and sizes to guarantee data integrity
│   └── raw/
│       └── hour.csv        # Frozen raw dataset (snapshot)
├── bike_demand/            # Python source code
│   ├── __init__.py
│   ├── preflight.py        # Environment and snapshot verification scripts
│   ├── split.py            # Data partitioning (Train/Val/Test)
│   ├── team.py             # Team naming utilities
│   ├── tracking.py         # MLflow recording and local storage
│   ├── train.py            # Training and evaluation pipeline
│   └── validate.py         # Strict data schema validation
├── .github/workflows/
│   └── ci.yml              # Continuous integration
├── uv.lock                 # Dependency lock file
└── pyproject.toml          # Package and dependency declarations
```

*(Note: The `artifacts/`, `reports/`, and `tracking/` directories will be generated automatically during execution).*

## Work to be Done (Expected Failures)

Several critical functions currently raise a `NotImplementedError`. This is the core task of Lab 2. You must complete the code in the following files:

1. **`validate.py`**: Complete `check_domains()` to validate value domains, finite ranges, and date windows.
2. **`split.py`**: Implement `split_data()` to assign sorted, non-empty, disjoint, and complete partitions chronologically.
3. **`train.py`**:
   * `select_features()`: Correctly filter the predictors (excluding labels and identities).
   * `compare_mean()`: Fit the comparator on training targets to create a naive baseline.
   * `fit_evaluate()`: Fit the Random Forest model on the train set and evaluate it strictly on validation rows.

## Execution Commands

### 1. Environment Verification (Preflight)

Before starting, verify that your environment, dependencies, and data integrity are correct:

```bash
python -m bike_demand.preflight
```

### 2. Data Validation

To test only your schema validation rules on the input CSV file:

```bash
python -m bike_demand.validate --data data/raw/hour.csv
```

### 3. Training

Once the TODOs are completed, run the full training pipeline using the provided configuration file:

```bash
python -m bike_demand.train --config configs/baseline.yaml
```

The models will be saved in `artifacts/`, the metrics in `reports/`, and the MLflow logs in `tracking/mlflow.db`.
