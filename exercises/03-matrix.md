# 03 · Matrix builds

**Learn:** `strategy.matrix`, `include`/`exclude`, `fail-fast`, multiple OSes, dynamic job names.

| Jenkins | GitHub Actions |
|---|---|
| `matrix { axes { axis { name 'PY'; values '3.11','3.12' } } }` | `strategy.matrix.python: ["3.11", "3.12"]` |
| `excludes { }` | `exclude:` |
| `failFast true` in `parallel` | `fail-fast: true` (the **default**!) |

## Tasks
- [ ] Test on Python `3.11`, `3.12`, `3.13` × `ubuntu-latest`, `windows-latest`.
- [ ] Exclude `windows + 3.11`.
- [ ] Set `fail-fast: false` and explain to yourself why that's usually what you want for test matrices.
- [ ] Give jobs readable names like `test (py3.12, ubuntu-latest)`.

## Done when
5 parallel jobs appear (3×2 − 1).

## Stretch
- Add one `include:` entry that adds an extra variable (e.g. `experimental: true`) to a single combo, and use `continue-on-error: ${{ matrix.experimental == true }}`.
- Add `macos-latest`. Note: on private repos, macOS minutes are billed at a much higher rate than Linux. Standard runners are free for public repos.

Solution: [`solutions/03-matrix.yml`](../solutions/03-matrix.yml)
