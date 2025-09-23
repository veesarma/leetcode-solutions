# LeetCode Solutions (uv + Docker)

A clean, reproducible Python repo for LeetCode solutions with tests, managed by **uv**, and runnable via Docker.

## Quickstart (local)

```bash
uv sync
uv run leetcode --help
uv run leetcode list
uv run leetcode run two-sum --input '{"nums":[2,7,11,15],"target":9}'
uv run pytest -q

