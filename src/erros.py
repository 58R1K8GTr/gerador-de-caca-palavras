"""Tratar erros com funções isoladas."""

from typing import Callable, TypeVar

T = TypeVar('T')


def erro_entrada_dimensao(funcao: Callable[[], T]) -> T | None:
    """Executa a função e retorna seu resultado, tratando erros."""
    try:
        return funcao()
    except (ValueError, TypeError):
        return print(
            "Formato de entrada errado. Apenas 2 "
            "números separados por espaço"
        )
