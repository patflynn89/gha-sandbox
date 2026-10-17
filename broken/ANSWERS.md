# Answers - don't peek until you've tried! 🙈

| # | Root cause | Fix |
|---|-----------|-----|
| B1 | Job has no `runs-on`. Every job needs a runner (Jenkins: like a stage with no `agent`). | Add `runs-on: ubuntu-latest`. |
| B2 | No `actions/checkout`. Runners start **empty** - unlike Jenkins' Multibranch, nothing is checked out automatically. | Add `- uses: actions/checkout@v7` as the first step. |
| B3 | Two bugs: the step has no `id: calc`, and it writes to `$GITHUB_ENV` (env var for later *steps in the same job*) instead of `$GITHUB_OUTPUT`. | `id: calc` + `echo "version=1.2.3" >> "$GITHUB_OUTPUT"`. |
| B4 | Matrix key is `python`, but referenced as `matrix.python-version` → evaluates to empty → setup-python falls back to the default. | Use `${{ matrix.python }}`. `actionlint` catches this. |
| B5 | `permissions:` only grants `contents: read`. Setting any permission sets all others to `none`. | Add `packages: write`. |
| B6 | `secrets` context is not available in `if:` conditions. | Map it into env first: job-level `env: HAS_HOOK: ${{ secrets.SLACK_WEBHOOK != '' }}` then `if: env.HAS_HOOK == 'true'`, and pass the secret via `env:` to the step. |
| B7 | **Script injection.** `${{ }}` is pasted into the shell script *before* bash runs. An attacker-controlled PR title becomes code. | Pass via env: `env: { TITLE: "${{ github.event.pull_request.title }}" }` and `run: echo "Thanks for the PR: $TITLE"`. Rule: never put untrusted `${{ github.event.* }}` directly in `run:`. |
| B8 | A job whose dependency was **skipped** is skipped too (implicit `success()`). | `if: ${{ !failure() && !cancelled() && needs.test-linux.result == 'success' }}` on `deploy`. |

Validate your fixes locally:
```bash
actionlint .github/workflows/*.yml
```
