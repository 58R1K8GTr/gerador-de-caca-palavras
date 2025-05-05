"""Entrada de usuário."""


from pathlib import Path

from src.utilitarios import fazer_ate
from src.erros import erro_entrada_dimensao


TEXTO_ENTRADA_DIMENSAO = (
    'Digite o tamanho do caça-palavras (formato: "N N"): '
)

TEXTO_ENTRADA_LOCAL_ARQUIVO = (
    'Digite o local do arquivo que contém as palavras '
    'ou arraste ele para o terminal: '
)


def pegar_dimenssoes() -> tuple[int, int]:
    """Pega e retorna as dimensões do usuário."""
    tamanho = fazer_ate(lambda: input(TEXTO_ENTRADA_DIMENSAO))
    tamanho = erro_entrada_dimensao(
        lambda: tuple(map(int, tamanho.strip().split(' ')))
    )
    return tamanho


def pegar_local_arquivo() -> Path:
    """Retorna o local do arquivo."""
    local_arquivo = fazer_ate(lambda: input(TEXTO_ENTRADA_LOCAL_ARQUIVO))
    return Path(local_arquivo.strip().strip("'"))
