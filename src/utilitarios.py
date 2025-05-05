"""Conjunto de funções sem um local definido úteis para o programa."""


from typing import Callable


def fazer_ate(funcao: Callable):
    """Função que executa outra função até ela retornar algo."""
    resultado = funcao()
    while any((not resultado, resultado is None)):
        resultado = funcao()
    return resultado
