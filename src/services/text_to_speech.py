from logging import Logger, getLogger
from pathlib import Path
from typing import Self
from uuid import uuid4

from elevenlabs import ElevenLabs, VoiceSettings
from gradio import Error

from utils.settings import Settings, settings


_STEPS: tuple[str] = ('app', 'elevenlabs')


class TextToSpeech:

    def __init__(self: Self, settings: Settings=settings):
        self.__settings: Settings = settings
        self.__debug: bool = settings.config('app', 'debug_mode')
        self.__verbose: bool = settings.config('app', 'verbose_mode')
        self.__logger: Logger = getLogger(__name__)

        self.__stability = settings \
            .config(*_STEPS, 'voice_settings', 'stability')
        self.__similarity_boost = settings \
            .config(*_STEPS, 'voice_settings', 'similarity_boost')
        self.__style = settings \
            .config(*_STEPS, 'voice_settings', 'style')
        self.__use_speaker_boost = settings \
            .config(*_STEPS, 'voice_settings', 'use_speaker_boost')

        self.__voice_id: str = self.__settings \
            .config(*_STEPS, 'voice_id')

        self.__model_id: str = self.__settings \
            .config(*_STEPS, 'model_id')

        self.__output_format: str = self.__settings \
            .config(*_STEPS, 'output_format')

        save_path_value: str = self.__settings \
            .config(*_STEPS, 'save_path')
        self.__save_path: Path = Path(save_path_value)
        self.__save_path.mkdir(parents=True, exist_ok=True)

        self.__optimize_streaming_latency: int = self.__settings \
            .config(*_STEPS, 'optimize_streaming_latency')

        self.__11labs: ElevenLabs = ElevenLabs(
            api_key=self.__settings.config('ELEVENLABS_API_KEY')
        )


    def generate(self: Self, text: str) -> Path:
        try:
            self.__logger.debug(f'Generating speech for "{text}"')

            response = self.__11labs.text_to_speech.convert(
                voice_id=self.__voice_id,
                optimize_streaming_latency=self.__optimize_streaming_latency,
                output_format=self.__output_format,
                text=text,
                model_id=self.__model_id,
                voice_settings=VoiceSettings(
                    stability=self.__stability,
                    similarity_boost=self.__similarity_boost,
                    style=self.__style,
                    use_speaker_boost=self.__use_speaker_boost
                ),

            )

            audio_filepath = self.__save_path / f'{uuid4()}.mp3'

            self.__logger.debug(f'Saving into {audio_filepath}')

            with open(audio_filepath, 'wb') as file_ref:
                for chunk in response:
                    if chunk:
                        file_ref.write(chunk)

            self.__logger.debug(f'File saved into {audio_filepath}')

            return audio_filepath

        except Exception as err:
            self.__logger.exception(
                f'Exception generating speech: {err}',
                exc_info=self.__debug or self.__verbose
            )

            raise Error('An unexpected error occurred generating speech')
