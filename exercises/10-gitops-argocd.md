# 10 · GitOps with Argo CD (local Kubernetes)

**Learn:** the core GitOps idea. **CI builds an image and changes Git. It never touches the cluster.** A controller in the cluster (Argo CD) pulls the desired state from Git and makes it so.

```
 push app code ──► GitHub Actions ──► build & push image to GHCR
                                  └─► commit new tag to gitops/base/kustomization.yaml
                                                      │
               Kubernetes ◄── Argo CD syncs ◄─────────┘ (polls Git every ~3 min)
```

| Jenkins "push" CD | GitOps "pull" CD |
|---|---|
| Jenkins has cluster credentials, runs `kubectl apply` | Cluster pulls from Git; CI has **no** cluster credentials |
| State of prod = whatever last ran | State of prod = **what's in Git** (audit log = `git log`) |
| Rollback = rerun old build | Rollback = `git revert` |
| Manual drift goes unnoticed | `selfHeal` reverts drift automatically |

## Prerequisites
```bash
brew install kind argocd          # kubectl ships with Docker Desktop
kind create cluster --name gha-sandbox
```

## Install Argo CD
```bash
kubectl create namespace argocd
kubectl apply -n argocd --server-side --force-conflicts \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl -n argocd rollout status deploy/argocd-server

# UI at https://localhost:8080  (user: admin)
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d; echo
kubectl -n argocd port-forward svc/argocd-server 8080:443
```

## Tasks
- [ ] Make sure exercise 08 pushed an image, and make the GHCR package **public** (kind can't pull private images without a pull secret).
- [ ] In `gitops/base/kustomization.yaml`, replace `CHANGE_ME` with your user and set `newTag` to an existing tag.
- [ ] In `gitops/argocd/application.yaml`, set `repoURL` to your repo. Apply it: `kubectl apply -n argocd -f gitops/argocd/application.yaml`.
- [ ] Watch Argo CD create the `shopcart` namespace + deployment. Verify:
      `kubectl -n shopcart port-forward svc/shopcart 9090:80` → `curl localhost:9090/version`
- [ ] Write the workflow: on change in `app/**` → build & push image tagged `sha-<short>` → `sed` the new tag into `kustomization.yaml` → commit & push as `github-actions[bot]`.
- [ ] Change something in the app, push, and watch the new version roll out **without running kubectl yourself**.

> ⚠️ If you required PRs on `main` in exercise 02, the bot's direct push will be rejected. Options: put `gitops/` in a separate repo (the common real-world setup), have the bot open a PR instead, or adjust the ruleset.

## Experiments (this is where it clicks)
- **Drift:** `kubectl -n shopcart scale deploy/shopcart --replicas=5`. Watch selfHeal set it back to 2.
- **Rollback:** `git revert` the bot's last commit. Argo CD rolls back.
- **Prune:** delete `service.yaml` from kustomization resources and push. The Service disappears.

## Why doesn't the bot commit trigger an infinite loop?
1. The workflow only triggers on `app/**`, and the bot only changes `gitops/**`.
2. Pushes made with `GITHUB_TOKEN` **never** trigger new workflow runs (GitHub's built-in loop protection).

## Stretch
- Split into `gitops/overlays/staging` and `overlays/production` (kustomize overlays), with prod promoted via **PR** instead of direct commit.
- Real-world layout: app code and deployment config in **separate repos**.
- Try [Flux](https://fluxcd.io/), the other big GitOps tool, with the same manifests.

## Cleanup
```bash
kind delete cluster --name gha-sandbox
```

Solution: [`solutions/10-gitops-deploy.yml`](../solutions/10-gitops-deploy.yml)
