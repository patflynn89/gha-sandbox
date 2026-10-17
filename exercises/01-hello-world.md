# 01 · Hello World: your first workflow

**Learn:** workflow file anatomy, triggers, jobs, steps, contexts, default env vars.

| Jenkins | GitHub Actions |
|---|---|
| `Jenkinsfile` | `.github/workflows/*.yml` (any number of files!) |
| `pipeline { agent any }` | `jobs.<id>.runs-on: ubuntu-latest` |
| `stage('x') { steps { sh '...' } }` | `steps: - name: x  run: ...` |
| `env.BRANCH_NAME`, `env.GIT_COMMIT` | `github.ref_name`, `github.sha` (or `$GITHUB_REF_NAME`, `$GITHUB_SHA`) |
| "Build with Parameters" button | `on: workflow_dispatch` |

## Tasks
- [ ] Create `.github/workflows/01-hello.yml` that runs on every `push`.
- [ ] One job, `ubuntu-latest`, one step that prints `Hello from <your user> on <branch>`.
- [ ] Add a second step that prints `$RUNNER_OS`, `$GITHUB_WORKSPACE` and the commit SHA.
- [ ] Add `workflow_dispatch` so you can also start it from the **Actions** tab.
- [ ] Push it and find the logs in the Actions tab.

## Done when
A green run appears in the Actions tab and you can start it manually.

## Stretch
- Use a multi-line `run: |` block.
- Dump the entire `github` context: `run: echo '${{ toJSON(github) }}'` and browse what's available.
- Run it locally: `act push -W .github/workflows/01-hello.yml`

Solution: [`solutions/01-hello.yml`](../solutions/01-hello.yml)
