"""Implementação da classe palavra."""


from random import choice

from src.letra import Letra


class Palavra:
    """Classe container que contém classes Letras."""

    CORES = [
        "bright_red", "bright_green", "bright_yellow",
        "bright_blue", "bright_magenta", "bright_cyan",
    ]

    def __init__(self, texto: str, x: int, y: int, direcao: tuple[int, int]):
        self.__texto = texto
        self.__x = x
        self.__y = y
        self.__direcao = direcao
        self.__letras: list[Letra] = []

    def adicionar_letra(self, letra: Letra) -> None:
        """Adiciona uma letra à palavra."""
        self.__letras.append(letra)

    def colorir(self) -> None:
        """Colore todas as letras da palavra."""
        cor = choice(self.CORES)
        for letra in self.__letras:
            letra.colorir(cor)

    def __len__(self) -> int:
        """Devolve o tamanho da palavra e não o tamanho da lista de letras."""
        return len(self.__texto)

    @property
    def texto(self) -> str:
        """Retorna a palavra em string."""
        return self.__texto

    @property
    def x(self) -> int:
        """Retorna a coordenada do x."""
        return self.__x

    @property
    def y(self) -> int:
        """Retorna a coordenada do y."""
        return self.__y

    @property
    def posicao_inicial(self) -> tuple[int, int]:
        """Retorna as coordenadas em tupla[x, y]"""
        return (self.__x, self.__y)

    @property
    def direcao(self) -> tuple[int, int]:
        """Retorna a direcao."""
        return self.__direcao

    @property
    def posicao_final(self) -> tuple[int, int]:
        """Retorna as posições do fim da palavra."""
        fim_x = self.__x + (len(self) - 1) * self.__direcao[0]
        fim_y = self.__y + (len(self) - 1) * self.__direcao[1]
        return (fim_x, fim_y)

    def __repr__(self) -> str:
        return f"Palavra({self.__texto})"
