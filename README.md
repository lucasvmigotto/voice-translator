---
title: Voice Translator
emoji: 💻
colorFrom: purple
colorTo: indigo
sdk: gradio
sdk_version: 4.44.0
app_file: src/app.py
pinned: false
---

# voice-translator

Voice to voice translator based in [AssemblyAI-Community/Voice-to-Voice-translator](https://github.com/AssemblyAI-Community/Voice-to-Voice-translator) project.

## Pre-requisites

* [Docker CE](https://docs.docker.com/engine/install/)
* [DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)
  * [Tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)
* [Dev Cotainers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* [AssemblyAI Api Key](https://www.assemblyai.com/dashboard/signup)
* [ElevenLabs Api Key](https://elevenlabs.io/app/sign-up)

## Development

1. Create a copy of `.env.example` names as `.env`

    > Place your Api Keys here

2. Press `CTRL` + `P` (or `F11`) and select _Dev Containers: Rebuild Container Without Cache_

3. Install dependencies:

    ```bash
    poetry install
    ```

4. Happy coding 😄

## Running

* To start the application, run the following command:

  ```bash
  poetry run python src/app.py
  ```

## Deploy

### Docker Image

* Define some env vars

    ```bash
    CONTAINER_REPOSITORY='us-central1-docker.pkg.dev/voice-translator/voice-translator'
    IMAGE_NAME='voice-translator'
    TAG="$(git describe --tags --abbrev=0)"
    CONTAINER_PUSH_NAME="${CONTAINER_REPOSITORY}/${IMAGE_NAME}:${TAG}"
    ```

* Build the image

    ```bash
    docker build \
      -f Dockerfile \
      --tag "${CONTAINER_PUSH_NAME}" \
      --progress plain \
      --no-cache \
      --debug \
      .
    ```

* Test the image

    ```bash
    docker run \
      --rm \
      --name 'voice-translator-container-test' \
      --env ELEVENLABS_API_KEY='<Your API Key>' \
      --env ASSEMBLYAI_API_KEY='<Your API Key>' \
      --publish 7860:7860 \
      --network bridge \
      "${CONTAINER_PUSH_NAME}"
    ```

    > Use `docker container rm -f $(docker container ls -qf 'name=voice-translator*')` to clean any running container

## Configurations

* To override any setting inside `application.toml`, set an _env var_ with the section(s) and key name

  > i.e. for the setting:
  >
  > ```toml
  > [app.logging]
  > level = 'DEBUG'
  > ```
  >
  > Set an _env var_ as:
  >
  > ```bash
  > export APP_LOGGING_LEVEL=INFO
  > ```

## References

* [Docker](https://docs.docker.com/)
* [DevContainers](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
* [Python](https://docs.python.org/3/)
* [Poetry](https://python-poetry.org/docs/)
* [AssemblyAI](https://www.assemblyai.com)
* [ElevenLabs](https://elevenlabs.io)
