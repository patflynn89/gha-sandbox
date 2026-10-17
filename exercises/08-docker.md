# 08 · Build & push a Docker image to GHCR

**Learn:** `GITHUB_TOKEN` + `permissions: packages: write`, Buildx, image tagging with `metadata-action`, Docker layer cache in GHA, not pushing on PRs.

| Jenkins | GitHub Actions |
|---|---|
| `docker.build(...)` / `docker.withRegistry(...)` | `docker/login-action` + `docker/build-push-action` |
| Registry credentials in Jenkins | `secrets.GITHUB_TOKEN` (auto-generated per run, no setup!) |

## Tasks
- [ ] Build `app/Dockerfile` on every PR (verify only) and **push** on `main`.
- [ ] Push to `ghcr.io/<your-user>/shopcart`.
- [ ] Tags: short SHA, branch name, PR number (via `docker/metadata-action@v6`).
- [ ] Pass `APP_VERSION=${{ github.sha }}` as build-arg.
- [ ] Enable the GHA layer cache (`cache-from/to: type=gha`). Compare build times between run 1 and run 2.

## Done when
The image shows under your GitHub profile → **Packages**, and this works:
```bash
docker run --rm -p 8080:8080 ghcr.io/<you>/shopcart:main
curl localhost:8080/version
```
(Make the package **public** in its settings, or `docker login ghcr.io` first.)

## Stretch
- Multi-arch: `platforms: linux/amd64,linux/arm64` (+ `docker/setup-qemu-action`).
- Scan the image with Trivy (`aquasecurity/trivy-action`) and fail on CRITICAL.

Solution: [`solutions/08-docker.yml`](../solutions/08-docker.yml)
