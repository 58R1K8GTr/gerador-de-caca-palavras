"""Implementação da classe palavra."""


class Palavra:
    """Classe container que contém classes Letras."""

    def __init__(self, palavra: str, x: int, y: int, direcao: tuple[int, int]):
        self.__palavra = palavra
        self.__x = x
        self.__y = y
        self.__direcao = direcao

    def __len__(self) -> int:
        """Devolve o tamanho da palavra e não o tamanho da lista de letras."""
        return len(self.__palavra)

    @property
    def palavra(self) -> str:
        """Retorna a palavra em string."""
        return self.__palavra[:]

    @property
    def x(self) -> int:
        """Retorna a coordenada do x."""
        return self.__x

    @property
    def y(self) -> int:
        """Retorna a coordenada do y."""
        return self.__y

    @property
    def posicao(self) -> tuple[int, int]:
        """Retorna as coordenadas em tupla[x, y]"""
        return (self.__x, self.__y)

    @property
    def direcao(self) -> tuple[int, int]:
        """Retorna a direcao."""
        return self.__direcao

    @property
    def fim(self) -> tuple[int, int]:
        """Retorna as posições do fim da palavra."""
        fim_x = self.__x + (len(self) - 1) * self.__direcao[0]
        fim_y = self.__y + (len(self) - 1) * self.__direcao[1]
        return (fim_x, fim_y)

    def __repr__(self) -> str:
        return f"Palavra({self.__palavra})"
