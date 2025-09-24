.PHONY: setup test lint fmt precommit build run docker-run

setup:        ## Create/refresh local .venv and install deps
	uv sync

test:         ## Run unit tests
	uv run pytest -q

lint:         ## Lint with Ruff
	uv run ruff check .

fmt:          ## Format with Ruff & Black
	uv run ruff format .
	uv run black .

precommit:    ## Run all pre-commit hooks
	uv run pre-commit run --all-files

build:        ## Build Docker image
	docker build -t leetcode-solutions .

run:          ## Run a problem: make run PROBLEM=two-sum INPUT='{"nums":[2,7,11,15],"target":9}'
	uv run leetcode run $(PROBLEM) --input '$(INPUT)'

docker-run:   ## Run inside Docker: make docker-run CMD="list"
	docker run --rm -it leetcode-solutions $(CMD)
