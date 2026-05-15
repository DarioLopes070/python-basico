from pathlib import Path
import os


def retornar_tamanho_dos_diretorios(caminho, profundidade=1):
    for arquivo in caminho.glob("*"):
        print(f"{arquivo.name} ---> {os.path.getsize(arquivo)}")


caminho = Path.home() / "Documents"
# os.path.getsize(arquivo) ---> pegar tamanho do arquivo
retornar_tamanho_dos_diretorios(caminho, profundidade=1)