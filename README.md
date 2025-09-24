# 🧩 LeetCode Solutions (uv + Docker)

A **production-ready**, fully reproducible Python project for LeetCode solutions — with uv, Docker/Colima, CLI, tests, linting, and CI.

## 🚀 Quickstart

```bash
uv sync
uv run leetcode list
uv run leetcode run two-sum --input '{"nums":[2,7,11,15],"target":9}'
uv run pytest -q

