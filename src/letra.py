"""Implementação da classe Letra."""


class Letra:
    """Uma unidade de letra no caça-palavras."""

    def __init__(self, caractere: str, x: int, y: int):
        self.__caractere = caractere
        self.__x = x
        self.__y = y
        self.__fixa = False

    def __str__(self) -> str:
        return str(self.__caractere)

    @property
    def fixa(self) -> bool:
        """Retorna um boolean caso pertença a uma palavra."""
        return self.__fixa

    @property
    def x(self) -> int:
        """Retorna a coordenada x."""
        return self.__x

    @property
    def y(self) -> int:
        """Retorna a coordenada y."""
        return self.__y

    @property
    def posicao(self) -> tuple[int, int]:
        """Retorna as coordenadas em tupla[x, y]."""
        return (self.__x, self.__y)

    def definir_caractere(self, caractere: str) -> None:
        """Define a letra como fixa em uma palavra."""
        self.__caractere = caractere
        self.__fixa = True

    def colorir(self, cor: str) -> None:
        """Define a letra como fixa em uma palavra."""
        self.__caractere = f"[{cor}]{self.__caractere}[/{cor}]"

    @property
    def caractere(self) -> str:
        """Retorna o caractere em forma de Text."""
        return self.__caractere

    def __repr__(self) -> str:
        nao = ' não' if self.__fixa else ''
        return f"Letra({self.__caractere}),{nao} é palavra"
