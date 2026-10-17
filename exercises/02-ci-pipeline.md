# 02 · A real CI pipeline

**Learn:** `actions/checkout`, `uses:` vs `run:`, `with:`, `push` vs `pull_request`, branch & path filters, `working-directory`.

| Jenkins | GitHub Actions |
|---|---|
| Implicit SCM checkout | **Explicit** `- uses: actions/checkout@v7`. Runners start empty! |
| Plugins / Global Tool Config (`tools { }`) | Marketplace actions, e.g. `actions/setup-python@v7` |
| Multibranch + PR discovery | `on: pull_request` |
| `when { changeset "app/**" }` | `on.push.paths: ["app/**"]` |
| `dir('app') { ... }` | `defaults.run.working-directory: app` |

## Tasks
- [ ] Workflow runs on push to `main` **and** on pull requests.
- [ ] It only triggers when files under `app/` (or the workflow itself) change.
- [ ] Steps: checkout → setup Python 3.13 → `pip install -e ".[dev]"` → `ruff check .` → `pytest -v`.
- [ ] Create a branch, **break a test on purpose** (`app/tests/test_cart.py`), open a PR and watch it fail. Fix it, watch it go green.
- [ ] In repo **Settings → Rules → Rulesets**, require this check to pass before merging to `main`.

## Done when
A PR with a failing test cannot be merged.

## Stretch
- Change only `README.md` in a PR: confirm the workflow does **not** run.
- Add a status badge to the README (Actions tab → workflow → `...` → *Create status badge*).

Solution: [`solutions/02-ci.yml`](../solutions/02-ci.yml)
