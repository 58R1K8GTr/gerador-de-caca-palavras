"""Implementação da classe Direção."""

from enum import Enum


class Direcao(Enum):
    """
    Representa as direções possíveis para inserir palavras no caça-palavras.

    Cada direção é uma tupla (dx, dy), onde:
    - dx: deslocamento vertical (linha)
    - dy: deslocamento horizontal (coluna)

    As direções seguem o padrão de uma matriz:
    - CIMA:           sobe      (-1,  0)
    - BAIXO:          desce     ( 1,  0)
    - ESQUERDA:       vai p/ esq (0, -1)
    - DIREITA:        vai p/ dir (0,  1)
    - DIAGONAL_CIMA_ESQ:     ↖ (-1, -1)
    - DIAGONAL_CIMA_DIR:     ↗ (-1,  1)
    - DIAGONAL_BAIXO_ESQ:    ↙ ( 1, -1)
    - DIAGONAL_BAIXO_DIR:    ↘ ( 1,  1)
    """
    CIMA = (-1, 0)
    BAIXO = (1, 0)
    ESQUERDA = (0, -1)
    DIREITA = (0, 1)
    DIAGONAL_CIMA_ESQ = (-1, -1)
    DIAGONAL_CIMA_DIR = (-1, 1)
    DIAGONAL_BAIXO_ESQ = (1, -1)
    DIAGONAL_BAIXO_DIR = (1, 1)
