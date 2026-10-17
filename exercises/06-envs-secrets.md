# 06 · Environments, secrets, conditions & approvals

**Learn:** repo vs environment secrets, `vars`, `environment:` with protection rules, `workflow_dispatch` inputs, `if:`, `concurrency`, `permissions`.

| Jenkins | GitHub Actions |
|---|---|
| Credentials + `withCredentials([...])` | `secrets.NAME` → pass via `env:` |
| `input message: 'Deploy?'` | Environment with **Required reviewers** |
| `parameters { choice(...) booleanParam(...) }` | `workflow_dispatch.inputs` (`type: choice`, `boolean`) |
| `when { branch 'main' }` | `if: github.ref == 'refs/heads/main'` |
| `disableConcurrentBuilds()` | `concurrency: { group: ..., cancel-in-progress: ... }` |
| `post { failure { } }` | job with `if: failure()` + `needs:` |

## Setup (in GitHub UI)
1. **Settings → Environments → New**: `staging` and `production`.
2. In both: add secret `DEPLOY_TOKEN` (any fake value) and variable `REGION`.
3. In `production`: enable **Required reviewers** (yourself) and restrict to branch `main`.

## Tasks
- [ ] Push to `main` → auto-deploys to **staging**.
- [ ] Manual run with inputs `target` (staging/production) and `dry_run` (boolean).
- [ ] Production deploy only via manual run from `main`, and **waits for your approval**.
- [ ] Echo the secret and confirm it's shown as `***` in logs.
- [ ] Add a job that only runs if a deploy failed.
- [ ] Set top-level `permissions: contents: read` (least privilege).

## Done when
A production run pauses with "Waiting for review" and continues after you approve.

## Stretch
- Read [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions). Then do debugging exercise **B7**.

Solution: [`solutions/06-envs-secrets.yml`](../solutions/06-envs-secrets.yml)
