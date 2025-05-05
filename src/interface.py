"""Implementação da interface com o usuário."""


from pathlib import Path

from click import command, argument, option
from rich import print as rich_print

from src.arquivo import ler_arquivo_com_filtro
from src.quadro import Quadro


@command()
@argument('altura', type=int)
@argument('largura', type=int)
@argument('arquivo', type=Path)
@option('--colorido/--nao-colorido', is_flag=True, default=True)
@option('-v', '--verboso', is_flag=True)
def cli_main(
    altura: int, largura: int, arquivo: Path, colorido: bool, verboso: bool
) -> None:
    """
    Programa cli que cria caça-palavras.

    regras do arquivo com palavras:\n
        - cada palavra em uma linha
    """
    palavras = ler_arquivo_com_filtro(
        lambda x: any((x == '', ' ' in x)), arquivo
    )
    caca_palavras = Quadro(largura, altura, colorido)
    for palavra in palavras:
        adicionada = caca_palavras.adicionar_palavra(palavra)
        if verboso:
            nao = '[green]' if adicionada else ' [red]não'
            rich_print(f"palavra {palavra}{nao} adicionada[/]")
    rich_print(caca_palavras.gerar_texto())
