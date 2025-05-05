"""Módulo principal."""


from contextlib import suppress
from src.interface import main


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        main()
