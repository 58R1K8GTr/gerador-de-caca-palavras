"""Gerenciamento de arquvos."""


from typing import Callable
from pathlib import Path


def ler_arquivo_com_filtro(filtro: Callable, local: Path) -> list[str]:
    """Lê um arquivo e retorna o conteúdo filtrado."""
    with local.open('r', encoding='utf8') as arquivo:
        bruto = filter(lambda x: not filtro(x), arquivo.readlines())
        palavras = list(map(lambda x: x.strip(), bruto))
    return palavras
