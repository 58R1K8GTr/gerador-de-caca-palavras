"""Implementação da interface com o usuário."""


from rich import print as rich_print

from src.entrada import pegar_dimenssoes, pegar_local_arquivo
from src.arquivo import ler_arquivo_com_filtro
from src.utilitarios import fazer_ate
from src.quadro import Quadro


def main():
    """Função principal que interage com o usuário."""
    print(
        'O arquivo deve conter somente as palavras que serão procuradas',
        'e também conter uma palavra por linha.'
    )
    tamanho = fazer_ate(pegar_dimenssoes)
    local_arquivo = pegar_local_arquivo()
    palavras = ler_arquivo_com_filtro(
        lambda x: any((x == '', ' ' in x)), local_arquivo
    )
    caca_palavras = Quadro(*tamanho)
    for palavra in palavras:
        adicionada = caca_palavras.adicionar_palavra(palavra)
        nao = '' if adicionada else ' não'
        print(f"palavra '{palavra}'{nao} adicionada")
    rich_print(caca_palavras.gerar_texto())
