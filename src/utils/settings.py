from os import getenv
from pathlib import Path
from typing import Any

from tomli import load as load_toml


def _get_config(data, *keys) -> Any | None:
    if isinstance(data.get(keys[0]), dict):
        return _get_config(data.get(keys[0]), *keys[1:])
    else:
        return data.get(keys[0])


class Settings:

    def __init__(self, configfile: str = 'application.toml') -> None:
        with open(Path(configfile), 'rb') as file_ref:
            self.__config: dict[str, Any] = load_toml(file_ref)

    def config(self, *keys) -> Any | None:
        if (env := getenv('_'.join(keys).upper(), None)) is not None:
            return env
        else:
            return _get_config(self.__config, *keys)

settings = Settings()
