# 04 · Caching & artifacts

**Learn:** dependency caching, `upload-artifact` / `download-artifact`, passing files between jobs, `if: always()`.

| Jenkins | GitHub Actions |
|---|---|
| Persistent workspace on the agent | Every job gets a **fresh VM**. Nothing is shared unless you say so. |
| `stash` / `unstash` | `actions/upload-artifact@v7` / `actions/download-artifact@v8` |
| `archiveArtifacts` | `upload-artifact` (downloadable from the run page) |
| `junit 'reports/*.xml'` | Upload the XML as an artifact (or use a test-report action) |
| `post { always { } }` | `if: always()` on a step |

## Tasks
- [ ] Turn on pip caching via `setup-python`'s `cache: pip` (hint: you need `cache-dependency-path`, since `pyproject.toml` lives in `app/`).
- [ ] Run pytest with `--junitxml=reports/junit.xml` and upload it as an artifact **even if tests fail**.
- [ ] Job `build`: `needs: test`, build a wheel (`python -m build --wheel`), upload `dist/*.whl`.
- [ ] Job `smoke`: `needs: build`, **no checkout**, download the wheel, `pip install` it, import it.

## Done when
The run page shows two downloadable artifacts, and the 2nd run's "Setup Python" step logs a cache hit.

## Stretch
- Use `actions/cache@v6` manually (key on `hashFiles('app/pyproject.toml')`) instead of the built-in option.

Solution: [`solutions/04-cache-artifacts.yml`](../solutions/04-cache-artifacts.yml)
