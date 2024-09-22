from logging import Logger, getLogger
from pathlib import Path
from typing import Self

from gradio import Error

from services.text_to_speech import TextToSpeech
from services.translate import Translate
from services.voice_to_text import VoiceToText
from utils.settings import Settings, settings


class VoiceToVoice:

    def __init__(self: Self, settings: Settings=settings):
        self.__settings: Settings = settings
        self.__debug: bool = settings.config('app', 'debug_mode')
        self.__verbose: bool = settings.config('app', 'verbose_mode')
        self.__logger: Logger = getLogger(__name__)

        self.__voice_to_text: VoiceToText = VoiceToText(self.__settings)
        self.__text_to_speech: TextToSpeech = TextToSpeech(self.__settings)


    def generate(self: Self, audio_file: Path | str) -> tuple[Path]:
        try:

            transcription: str = self.__voice_to_text.transcribe(audio_file)

            translations: list[dict[str, str]] = Translate.translate_text(transcription)

            generated_audio: list[dict[str, Path]] = []

            for translation in translations:
                generated_audio.append({
                    'language': translation.get('lang'),
                    'translation': translation.get('text'),
                    'audio_file': self.__text_to_speech.generate(
                        translation.get('text')
                    )
                })

            return tuple(generated['audio_file'] for generated in generated_audio)


        except Error as err:
            raise err

        except Exception as err:
            self.__logger.exception(
                f'Error generating voice to voice: {err}',
                exc_info=self.__debug or self.__verbose
            )
