# GitHub Actions & GitOps Sandbox 🧪

A hands-on practice repo for going from **Jenkins → GitHub Actions → GitOps**.
You get a tiny Python app (`app/`), 11 progressive exercises, reference solutions, 8 intentionally broken workflows to debug, and a local Kubernetes + Argo CD GitOps lab.

```
app/                  Tiny Python app (cart logic + stdlib HTTP server), tests, Dockerfile
exercises/            01 … 11: the tasks. START HERE
solutions/            Reference workflows (outside .github/ so they don't run)
broken/               Debugging challenges + ANSWERS.md
gitops/               Kustomize manifests + Argo CD Application (exercise 10)
.github/workflows/    ← YOUR workflows go here (empty on purpose)
```

## 1. Setup (5 min)

```bash
# Tools
brew install act actionlint       # run workflows locally + lint them
# (Docker Desktop must be running for act)

# Put this sandbox on GitHub as a PUBLIC repo (public = unlimited free Actions minutes)
git init -b main
git add . && git commit -m "Initial sandbox"
gh repo create gha-sandbox --public --source=. --push
```

App sanity check:
```bash
cd app && python3 -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]" && pytest && ruff check .
```

## 2. The loop

1. Read `exercises/NN-*.md`.
2. Write your workflow in `.github/workflows/`. **Don't look at the solution yet.**
3. `actionlint` → catch mistakes before pushing.
4. Optional: `act push -W .github/workflows/your.yml` for a fast local run.
5. Push. Read the logs in the **Actions** tab. Iterate.
6. Compare with `solutions/`. Differences are fine if you understand why.

> 💡 Practice on branches + PRs, not straight to `main`. That's how you'll work in a team, and it exercises `pull_request` triggers.

## 3. Roadmap

| # | Exercise | Key concepts |
|---|----------|--------------|
| 01 | [Hello World](exercises/01-hello-world.md) | anatomy, triggers, contexts |
| 02 | [CI pipeline](exercises/02-ci-pipeline.md) | checkout, setup-python, PRs, path filters, required checks |
| 03 | [Matrix](exercises/03-matrix.md) | multi-version / multi-OS |
| 04 | [Cache & artifacts](exercises/04-cache-artifacts.md) | caching, passing files between jobs |
| 05 | [Job graphs & outputs](exercises/05-jobs-outputs.md) | `needs`, outputs, job summaries |
| 06 | [Environments & secrets](exercises/06-envs-secrets.md) | secrets, approvals, inputs, `if:`, concurrency, permissions |
| 07 | [Reusable workflows](exercises/07-reusable.md) | composite actions, `workflow_call` (≈ Shared Libraries) |
| 08 | [Docker → GHCR](exercises/08-docker.md) | GITHUB_TOKEN, buildx, tagging, layer cache |
| 09 | [Release on tag](exercises/09-release.md) | tag triggers, GitHub Releases |
| 10 | [GitOps with Argo CD](exercises/10-gitops-argocd.md) | kind, Argo CD, pull-based deploys, drift, rollback |
| 11 | [Debugging](exercises/11-debugging.md) | 8 broken workflows |
| ★ | GitLab | Rewrite your pipeline as `.gitlab-ci.yml`, then compare with [`solutions/gitlab-ci-equivalent.yml`](solutions/gitlab-ci-equivalent.yml) |

## 4. Jenkins → GitHub Actions → GitLab cheat sheet

| Concept | Jenkins | GitHub Actions | GitLab CI |
|---|---|---|---|
| Pipeline file | `Jenkinsfile` (1) | `.github/workflows/*.yml` (many) | `.gitlab-ci.yml` (1, + `include:`) |
| Executor | `agent { label 'x' }` | `runs-on: ubuntu-latest` | `tags:` / `image:` |
| Unit of work | `stage` | `job` (parallel by default!) | `job` grouped into `stages` |
| Ordering | sequential stages | `needs:` | `stages:` order or `needs:` |
| Checkout | implicit | `actions/checkout` (explicit!) | implicit |
| Reuse | Shared Libraries | composite actions / reusable workflows | `include:` / `extends:` / CI components |
| Parameters | `parameters {}` | `workflow_dispatch.inputs` | `spec: inputs` / variables |
| Conditions | `when {}` | `if:` | `rules:` |
| Credentials | `withCredentials` | `secrets.X` | CI/CD variables (masked/protected) |
| Approval | `input` | environment required reviewers | `when: manual` / protected envs |
| Stash / archive | `stash`, `archiveArtifacts` | `upload-artifact` / `download-artifact` | `artifacts:` |
| Post actions | `post { always/failure }` | `if: always()` / `failure()` | `when: always` / `on_failure` |
| Matrix | `matrix { axes {} }` | `strategy.matrix` | `parallel: matrix:` |
| Plugins | Jenkins plugins | Marketplace actions | (mostly containers + scripts) |

## 5. Learn from real-world repos

Read their `.github/workflows/` folders. That's how pros write pipelines:

- **[actions/starter-workflows](https://github.com/actions/starter-workflows)**: official templates for every language
- **[astral-sh/ruff](https://github.com/astral-sh/ruff/tree/main/.github/workflows)**: large Python/Rust project; matrix, release, Docker, docs
- **[pydantic/pydantic](https://github.com/pydantic/pydantic/tree/main/.github/workflows)**: clean Python CI
- **[argoproj/argocd-example-apps](https://github.com/argoproj/argocd-example-apps)**: GitOps repo layouts (kustomize, helm, …)
- **[sdras/awesome-actions](https://github.com/sdras/awesome-actions)**: curated list of actions
- **[GitHub Skills](https://github.com/skills)** (e.g. `skills/hello-github-actions`): free, interactive courses that run *inside* a repo
- **[nektos/act](https://github.com/nektos/act)** · **[rhysd/actionlint](https://github.com/rhysd/actionlint)**: your local tooling

Docs: [GitHub Actions](https://docs.github.com/actions) · [Workflow syntax](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions) · [Argo CD](https://argo-cd.readthedocs.io/) · [GitLab CI](https://docs.gitlab.com/ci/)

## 6. Graduation project 🎓

Take a real project of yours (e.g. one you currently build with Jenkins) and give it:
CI on PRs → matrix tests → Docker image to GHCR → release on tag → GitOps deploy to kind via Argo CD, using **only** workflows you wrote yourself.
