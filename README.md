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

3. Happy coding 😄

## Running

* To start the application, run the following command:

  ```bash
  poetry run python src/main.py
  ```

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

* [Python](https://docs.python.org/3/)
* [Poetry](https://python-poetry.org/docs/)
* [AssemblyAI](https://www.assemblyai.com)
* [ElevenLabs](https://elevenlabs.io)
