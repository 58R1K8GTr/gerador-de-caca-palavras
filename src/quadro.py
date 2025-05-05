"""Implementação da classe CacaPalavras."""

from random import choice, shuffle
from string import ascii_uppercase
from itertools import chain

from src.letra import Letra
from src.palavra import Palavra
from src.direcao import Direcao
from src.tipos import DirecaoNoneTipo


# adicionando o ç nas letras
CARACTERES = ascii_uppercase + 'ÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÇ'


class Quadro:
    """Classe container que representa um quadro 2d."""
    def __init__(self, largura: int, altura: int):
        self.__largura = largura
        self.__altura = altura
        self.__matriz = [
            [
                Letra(choice(CARACTERES), x, y)
                for x in range(largura)
            ]
            for y in range(altura)
        ]
        self.__palavras: list[Palavra] = []
        self.__letras_impossiveis: set[Letra] = set()

    def adicionar_palavra(self, palavra: str) -> bool:
        """Adiciona uma palavra no quadro."""
        if len(palavra) > max((self.__altura, self.__largura)):
            return False
        posicoes = list(chain(*self.__matriz))
        shuffle(posicoes)  # remover vieses
        for letra_base in posicoes:
            direcao_escolhida = self.__direcao_valida(letra_base, palavra)
            if direcao_escolhida:
                self.__letras_impossiveis.add(letra_base)
                self.__inserir_palavra(
                    palavra, *letra_base.posicao, direcao_escolhida
                )
                return True
        return False

    def __direcao_valida(
        self, letra_base: Letra, palavra: str
    ) -> DirecaoNoneTipo:
        """Verifica se a letra base tem alguma direção válida."""
        direcoes = list(Direcao)
        shuffle(direcoes)  # remover vieses
        for direcao in direcoes:
            if self.__validar_insercao(
                palavra, *letra_base.posicao[:], direcao
            ):
                return direcao
        return None

    def __validar_insercao(
        self, palavra: str, x: int, y: int, direcao: Direcao
    ) -> bool:
        """Valida se a palavra inteira cabe na direção escolhida."""
        dx, dy = direcao.value
        for i in range(len(palavra)):
            nx, ny = x + i * dx, y + i * dy
            if not all((0 <= nx < self.__largura, 0 <= ny < self.__altura)):
                return False
            if self.__matriz[ny][nx].fixa:
                return False
        return True

    def __inserir_palavra(
        self, palavra: str, x: int, y: int, direcao: Direcao
    ):
        """Insere a palavra no quadro."""
        dx, dy = direcao.value
        for i, letra in enumerate(palavra):
            nx, ny = x + i * dx, y + i * dy
            self.__matriz[ny][nx].definir_letra(letra.upper())
        self.__palavras.append(Palavra(palavra, x, y, direcao.value))

    def largura(self) -> int:
        """Retorna a largura do quadro."""
        return self.__largura

    def altura(self) -> int:
        """Retorna a altura do quadro."""
        return self.__altura

    def gerar_texto(self) -> str:
        """Retorna uma matriz com os caracteres em string para a exibição."""
        return '\n'.join(
            ' '.join(map(lambda x: x.caractere, linha))
            for linha in self.__matriz
        )

    def __len__(self):
        """Retorna quantas palavras foram inseridas no quadro."""
        return len(self.__palavras)

    def __repr__(self) -> str:
        return f"Quadro(palavras: {len(self)})"
