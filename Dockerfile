# syntax=docker/dockerfile:1.7-labs

FROM python:3.12 as requirements-stage

WORKDIR /tmp

RUN pip install --quiet poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export \
    -f requirements.txt \
    --output requirements.txt \
    --without-hashes \
    --without dev

FROM python:3.12-slim

ARG GRADIO_PORT=7860

ENV APP_DEBUG_MODE=True
ENV APP_VERBOSE_MODE=True

# ENV ELEVENLABS_API_KEY=
# ENV ASSEMBLYAI_API_KEY=

ENV PYTHONPATH=/app/src

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --quiet \
    -r /app/requirements.txt \
    --no-cache-dir \
    --upgrade

COPY --parents ./src/ ./application.toml /app/

EXPOSE ${GRADIO_PORT}

CMD "python" "src/app.py"
