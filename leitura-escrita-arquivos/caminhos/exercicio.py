from pathlib import Path

# Script para encontrar um arquivo dentro da pasta  home do usuario

caminho = Path.home()

def encontra_arquivo(caminho, nome_do_arquivo):
    for arquivo in caminho.glob("**/*"):
        if arquivo.is_file():
            # if arquivo.name == nome_do_arquivo:
            if arquivo.stem == nome_do_arquivo:
                print(caminho)

encontra_arquivo(caminho, "arquivo_primeira_pasta")