# 11 · Debug broken workflows

In real life you'll spend more time fixing pipelines than writing them. [`broken/`](../broken/) has 8 workflows, each with one realistic bug and a **SYMPTOM** comment.

## How to work
1. Copy one into `.github/workflows/`, push, and observe the failure in GitHub.
2. Also run `actionlint` on it. Note which bugs a linter catches (B1, B3, B4, B6, B7) and which only show at runtime (B2, B5, B8).
3. Fix it. Check against [`broken/ANSWERS.md`](../broken/ANSWERS.md).

## Debugging toolbox
- **Re-run with debug logging:** "Re-run jobs" → ☑ *Enable debug logging* (or set repo secret/variable `ACTIONS_STEP_DEBUG=true`).
- **Dump contexts:** `run: echo '${{ toJSON(needs) }}'` (also `steps`, `matrix`, `github`).
- **Lint before push:** `actionlint`, or the GitHub Actions extension for VS Code (validation + autocomplete).
- **Run locally:** `act -j <job>` (fast feedback for shell logic; not 100% identical to GitHub).
- **SSH into a runner** (last resort): `mxschmitt/action-tmate` in a step.
