FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && ln -s /root/.local/bin/uv /usr/local/bin/uv

WORKDIR /app

# ---- dependency layer (cached unless lockfile/pyproject changes) ----
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# Ensure the venv is on PATH
ENV PATH="/app/.venv/bin:${PATH}"

# ---- app layer ----
COPY src ./src
COPY tests ./tests
COPY README.md .
COPY .python-version* . 2>/dev/null || true

# Default entrypoint is the CLI
ENTRYPOINT ["leetcode"]
CMD ["--help"]
