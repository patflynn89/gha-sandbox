# 05 · Job graphs, outputs & job summaries

**Learn:** `needs` (fan-out / fan-in), step `id` + `$GITHUB_OUTPUT`, job `outputs`, `$GITHUB_ENV`, `$GITHUB_STEP_SUMMARY`, `needs.<job>.result`.

| Jenkins | GitHub Actions |
|---|---|
| Stages run sequentially by default | Jobs run **in parallel** by default; order them with `needs:` |
| `parallel { }` | Just jobs without `needs` |
| Global `def version = ...` in Groovy | Step output → job output → `needs.<job>.outputs.<name>` |
| `env.FOO = 'x'` (later stages) | `echo "FOO=x" >> "$GITHUB_ENV"` (later **steps of the same job only**) |
| Build description / HTML publisher | `$GITHUB_STEP_SUMMARY` (Markdown rendered on run page) |

## Tasks
- [ ] Job `version` computes `<pyproject version>+<short sha>` and exposes it as a job output.
- [ ] Jobs `lint` and `test` run **in parallel**.
- [ ] Job `report` waits for all three and writes a Markdown table to the job summary with the version and the results of lint/test.

## Done when
The run's graph view shows the fan-out/fan-in diamond, and the summary table appears on the run page.

## Stretch
- Make `report` run even if `test` fails (hint: `if: always()`), and show ❌/✅ in the table.
- Generate a matrix **dynamically**: one job outputs a JSON list, another uses `strategy.matrix.python: ${{ fromJSON(needs.x.outputs.list) }}`.

Solution: [`solutions/05-jobs-outputs.yml`](../solutions/05-jobs-outputs.yml)
