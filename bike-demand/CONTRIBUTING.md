# Contributing to TeamA Bike Demand

This document describes how our team collaborates on the Bike Demand MLOps project.

## Team and responsibilities

- **Alexandre:** Lab 1 helper implementation, additional unit test, and local test evidence.
- **Thaddée:** Lab 1 primary code review, pull request approval and merge, and team working agreement.
- **Nicolas:** Shared repository setup, project README, and secondary verification.
- **Alban:** Project architecture and technical organization.

Responsibilities rotate between labs. The Lab 2 lead must be different from the Lab 1 lead. Each member contributes code, documentation, or a substantive review, and records their actual work in the team notes.

## Branches and commits

- Keep `main` as the shared integration branch. Do not commit directly to `main` for team project changes.
- Create a dedicated branch for each focused task, such as `fix/lab1-team-slug`, `docs/contributing-guide`, or `feat/lab2-validation`.
- Make small, reviewable commits with clear messages, for example `fix: normalize repeated whitespace in team names` or `docs: document contribution workflow`.
- Inspect `git status` and `git diff` before staging. Add only intended files.
- Do not commit credentials, private student reports, `.venv`, generated artifacts, or local MLflow tracking databases and models.

## Local setup and checks

Run project commands from the `bike-demand/` directory, using the approved starter and locked dependencies:

```bash
uv sync --locked
uv run --locked python -m bike_demand.preflight
uv run --locked pytest -q -m infra
uv run --locked pytest -q -m lab1
uv run --locked ruff check .
uv run --locked ruff format --check .
```

For Lab 2, also run the relevant Lab 2 tests and pipeline checks specified by the course instructions. Do not claim a check passed unless it was actually run successfully. Preserve the canonical source data and keep generated outputs out of Git.

## Pull requests and review

1. Push the task branch and open a pull request targeting `main`.
2. Describe the change, its motivation, relevant test results, and any known limitations. Link evidence when available.
3. Request a review from another team member. The author must not approve their own pull request.
4. The reviewer inspects the diff and tests, records at least one actionable observation, and checks the latest pushed revision. The author responds to the review and makes any needed changes.
5. Check GitHub Actions results for the latest commit, in addition to local test evidence. A missing workflow or missing checks must not be reported as a passing CI run.
6. Merge only after the required peer approval, relevant checks, and review discussion are complete. Update `main` locally after the merge.

## Communication and handover

- Report blockers to the team promptly, including the command, error message, and attempted fix, without exposing secrets.
- Use the course-approved support route for unresolved setup or repository access issues.
- Record actual responsibilities, test evidence, PR links, reviewer feedback, blockers, and next owners in the team reports.
- Use `WORKING-AGREEMENT.md` for the current team roles and coordination rules.
- The Week 1 team evidence covers Labs 1 and 2. Each student writes their own `reports/week-1.md` in their **private** repository, not in the shared project repository.
