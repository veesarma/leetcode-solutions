## Summary
- Initialize uv-managed Python repo for LeetCode
- Dockerized CLI to run problems by slug
- Tests + lint/format via CI

## What changed
- Project skeleton (src/, tests/, pyproject.toml)
- CLI: `leetcode list` / `leetcode run <slug>`
- Example problem `two_sum` + tests
- Dockerfile + .dockerignore
- GitHub Actions CI (ruff, black, pytest)

## Why
- Reproducible dev/test environment
- Easy run path for any problem
- Standardized lint/format/tests on PRs

## Checklist
- [ ] CI green (lint/format/tests)
- [ ] README updated if needed
- [ ] Problem + tests added/adjusted

## Screenshots/Logs
<!-- paste any outputs if relevant -->
