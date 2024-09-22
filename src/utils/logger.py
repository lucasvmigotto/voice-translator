from logging import basicConfig

from utils.settings import settings


_STEPS: tuple[str] = ('app', 'logging')
_LOG_LEVEL: str = settings.config(*_STEPS, 'level')
_LOG_DATE_FORMAT: str = settings.config(*_STEPS, 'date_format')
_LOG_FORMAT: str = settings.config(*_STEPS, 'format')


def setup_logging(
    level: str=_LOG_LEVEL,
    date_format: str=_LOG_DATE_FORMAT,
    format: str=_LOG_FORMAT,
) -> None:
    basicConfig(
        level=level,
        datefmt=date_format,
        format=format
    )
