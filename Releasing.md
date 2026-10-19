# Releasing
Features merge to `main` freely; releases are cut from `main` when there's something worth shipping.

## Feature workflow

1. `git switch main; git pull`
2. `git switch -c feature/short-name`
3. Commit as you go
4. Push, open a PR with a clear title (it becomes the release note), merge on GitHub
5. Delete the branch

Don't touch the version in feature branches.

## Release workflow

1. `git switch main; git pull`
2. Preview: `uv version --bump minor --dry-run`
3. Bump: `uv version --bump minor`
4. Commit: `git commit -am "Release v$(uv version --short)"`
5. Tag: `git tag -a "v$(uv version --short)" -m "v$(uv version --short)"`
6. Push: `git push; git push --tags`
7. GitHub → Releases → Draft new release → pick the tag → **Generate release notes** → Publish

`uv version --bump` updates both `pyproject.toml` and `uv.lock`; make sure `uv.lock` is tracked so `-a` picks it up.

## Which bump?

| Change | Bump | Example |
|---|---|---|
| Bug fixes only | `patch` | 0.3.1 → 0.3.2 |
| New features, or breaking changes (pre-1.0) | `minor` | 0.3.2 → 0.4.0 |
| Stable API commitment / breaking change post-1.0 | `major` | 0.9.0 → 1.0.0 |

## When to release

- When `main` has something you or someone else needs
- Before deploying anywhere
- Batching a few merges per release is fine

## Deploying a specific version

```powershell
git clone --branch v0.4.0 <repo-url>
```
