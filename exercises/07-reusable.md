# 07 · DRY: composite actions & reusable workflows

**Learn:** the two reuse mechanisms and when to use which.

| Jenkins Shared Library | GitHub Actions |
|---|---|
| `vars/setupApp.groovy` (custom step) | **Composite action**: `.github/actions/<name>/action.yml`, used as a **step** |
| Whole pipeline template (`buildPythonApp()`) | **Reusable workflow**: `on: workflow_call`, used as a **job** (`jobs.x.uses:`) |
| `@Library('lib@v1')` | `uses: org/repo/.github/workflows/x.yml@v1` |

**Rule of thumb:** a few steps you repeat → composite action. A whole job or pipeline you repeat → reusable workflow.

## Tasks
- [ ] Composite action `.github/actions/setup-app` that does setup-python (+cache) and installs the app. Input: `python-version`.
- [ ] Reusable workflow `.github/workflows/reusable-test.yml` (`on: workflow_call`) that uses the composite action, lints, tests, and exposes an output `passed`.
- [ ] Caller workflow that invokes it twice (3.12 and 3.13) and prints both outputs.

## Done when
The caller run shows nested jobs `test-312 / test` and `test-313 / test`.

## Stretch
- Move the reusable workflow to a **separate repo** (like a real shared library) and call it with `@main`. Then tag it `v1` and pin to that.
- Pass a secret to it with `secrets: inherit`.

Solution: [`solutions/07-reusable/`](../solutions/07-reusable/)
