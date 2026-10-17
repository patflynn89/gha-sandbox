# 09 · Release on tag

**Learn:** tag triggers, `GITHUB_REF_NAME`, `permissions: contents: write`, the `gh` CLI inside workflows, failing early with `::error::`.

## Tasks
- [ ] Trigger on tags matching `v*.*.*`.
- [ ] Fail if the tag (`v0.1.0`) doesn't match `version` in `app/pyproject.toml`.
- [ ] Test, build sdist + wheel, create a GitHub Release with auto-generated notes and the files attached.

Try it:
```bash
git tag v0.1.0 && git push origin v0.1.0     # should succeed
git tag v9.9.9 && git push origin v9.9.9     # should fail the version check
```

## Stretch
- Also push the Docker image tagged `0.1.0` and `latest` (metadata-action `type=semver,pattern={{version}}`).
- Look at [release-please](https://github.com/googleapis/release-please-action) to automate versioning from commit messages.

Solution: [`solutions/09-release.yml`](../solutions/09-release.yml)
