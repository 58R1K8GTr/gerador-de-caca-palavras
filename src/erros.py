"""Tratar erros com funções isoladas."""


from pathlib import Path

from rich import print as rich_print


def erro_entrada_arquivo(local: Path) -> list[str] | None:
    """Retorna o conteúdo de um arquivo sem erros, se possível."""
    forma = '[red]{}[/]'
    try:
        with local.open('r', encoding='utf8') as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        rich_print(forma.format('Insira um arquivo existente.'))
    except PermissionError:
        rich_print(forma.format(
            'O programa não tem permissões para abrir o arquivo.'
        ))
    except OSError:
        rich_print(forma.format('Erro inesperado.'))
    return None
