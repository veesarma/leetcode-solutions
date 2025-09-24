.PHONY: setup lock test lint fmt run build docker-run ci

# Create/refresh local .venv and install deps
setup:
	uv sync

# Pin dependencies
lock:
	uv lock

# Run unit tests
test:
	uv run pytest -q

# Lint (Ruff) and format-check (Black)
lint:
	uv run ruff check .
fmt:
	uv run black .

# Run a problem: make run PROBLEM=two-sum INPUT='{"nums":[2,7,11,15],"target":9}'
run:
	uv run leetcode run $(PROBLEM) --input '$(INPUT)'

# Build and run Docker (Colima/Docker Desktop must be running)
build:
	docker build -t leetcode-solutions .
docker-run:
	docker run --rm -it leetcode-solutions $(CMD)

# Simulate CI locally
ci: setup lint test
