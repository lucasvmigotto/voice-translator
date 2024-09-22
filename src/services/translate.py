from logging import Logger, getLogger

from translate import Translator

from utils.settings import settings


_DEBUG: bool = settings.config('app', 'debug_mode')
_VERBOSE: bool = settings.config('app', 'verbose_mode')
_ORIGINAL_LANGUAGE: str = settings.config('app', 'original_language')
_LANGUAGES: list[dict[str, str]] = settings.config('app', 'languages')
_logger: Logger = getLogger(__name__)


class Translate:

    @staticmethod
    def translate_text(text: str) -> list[dict[str, str]]:
        languages: list[dict[str, str]] = []
        try:
            _logger.info(
                f"Translating '{text}' to "
                ', '.join([lang['label'] for lang in _LANGUAGES])
            )

            for language in _LANGUAGES:

                _logger.debug(f'Translating to {language}')

                languages.append({
                    'lang': language['label'],
                    'text': Translator(
                        from_lang=_ORIGINAL_LANGUAGE,
                        to_lang=language['slug']
                    ).translate(text)
                })

        except Exception as err:
            _logger.exception(
                f'Exception: {err}',
                exc_info=_DEBUG or _VERBOSE
            )

        finally:
            return languages

