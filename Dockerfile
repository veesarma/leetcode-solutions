FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && ln -s /root/.local/bin/uv /usr/local/bin/uv

WORKDIR /app
COPY . .
RUN uv sync --frozen
ENV PATH="/app/.venv/bin:${PATH}"

ENTRYPOINT ["leetcode"]
CMD ["--help"]
