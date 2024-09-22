# syntax=docker/dockerfile:1

FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

ARG USERNAME="vscode"
ARG POETRY_VERSION="1.8.3"

USER ${USERNAME}

WORKDIR /app

RUN pipx install poetry==${POETRY_VERSION}

RUN pipx inject poetry poetry-plugin-export

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --with dev

ENV PYTHONPATH=/app/src
