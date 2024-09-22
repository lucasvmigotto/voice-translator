from logging import Logger, getLogger
from pathlib import Path
from typing import Self

from assemblyai import (
    Transcriber,
    Transcript,
    TranscriptionConfig,
    TranscriptStatus,
    settings,
)
from gradio import Error

from utils.settings import Settings


class VoiceToText:

    def __init__(self: Self, settings: Settings=settings):
        self.__settings: Settings = settings
        self.__debug: bool = settings.config('app', 'debug_mode')
        self.__verbose: bool = settings.config('app', 'verbose_mode')
        self.__logger: Logger = getLogger(__name__)

        settings.api_key = self.__settings.config('assemblyia_api_key')

        self.__original_language: str = settings \
            .config('app', 'original_language')

        self.__transcriber: Transcriber = Transcriber()


    def transcribe(self: Self, audio_file: Path | str) -> str:
        try:
            self.__logger.debug(f'Transcribing  "{audio_file}"')

            transcript: Transcript = self.__transcriber.transcribe(
                audio_file,
                config=TranscriptionConfig(
                    language_code=self.__original_language
                )
            )

            if transcript.status == TranscriptStatus.error:
                raise Error('Could not transcribe audio file')

            self.__logger.debug(f'Text from "{audio_file}": {transcript}')

            return transcript.text

        except Error as err:
            raise err

        except Exception as err:
            self.__logger.exception(
                f'Exception transcribing audio file to text: {err}',
                exc_info=self.__debug or self.__verbose
            )

            raise Error('An unexpected error occurred transcribing audio file')
