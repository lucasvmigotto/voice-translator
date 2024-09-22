from gui.demo import gui as demo
from utils.logger import setup_logging
from utils.settings import settings


setup_logging()

SERVER_NAME: str = settings.config('app', 'server', 'host')
SERVER_PORT: int = settings.config('app', 'server', 'port')
DEBUG_MODE: bool = settings.config('app', 'debug_mode')
VERBOSE_MODE: bool = settings.config('app', 'verbose_mode')


if __name__ == '__main__':
    demo.launch(
        server_name=SERVER_NAME,
        server_port=SERVER_PORT,
        debug=DEBUG_MODE or VERBOSE_MODE
    )
