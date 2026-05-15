from pathlib import Path
import os

""" -> OUTRA MANEIRA DE CRIAR VARIAS LINHAS DE COMENTARIO, AO INVES DE USAR # PODEMOS USAR 3X O (") PARA ABRIR E + 3X PARA FECHAR O COMENTÁRIO  
# Retornando o caminho do diretorio atual de trabalho
print(Path.cwd())

# esse Caminho é absoluto
print(Path.cwd().is_absolute())
# esse Caminho é absoluto
print(Path.cwd().is_absolute())

# Retornando caminho de primeira pasta
print(Path("primeira_pasta"))

# esse Caminho é absoluto
print(Path("primeira_pasta").is_absolute())

# Transformando o caminho em absoluto
print(Path.cwd() / "primeira_pasta")

# verifica se diretório existe
print((Path.cwd() / "primeira_pasta").exists())

# alterar diretório
os.chdir(Path.home()) 
# verifica se caminho ainda existe
print(Path.cwd() / "primeira_pasta")
print((Path.cwd() / "primeira_pasta").exists())

"""

 
"""
# Garantindo que estamos retornando o caminho para a pasta do script
print(__file__)
print(Path(__file__).is_absolute())
print(Path(__file__).parent)
print(Path(__file__).parent / "primeira_pasta")
print((Path(__file__).parent / "primeira_pasta").exists())
"""

caminho_arquivo = Path(__file__)
print(caminho_arquivo.anchor) # pasta raiz do sistema, normalmente o c:\
print(caminho_arquivo.parent) # possivel empilhar comandos parents -> print(caminho_arquivo.parent.parent.parent)
print(caminho_arquivo.name) # retorna nome do arquivo
print(caminho_arquivo.stem) # retorna a base do nome do arquivo, sem extensão
print(caminho_arquivo.suffix) # retorna a extensão do nome do arquivo
print(caminho_arquivo.drive) # retorna o nome do nosso disco

print(caminho_arquivo.parent) 
print(caminho_arquivo.parents[0]) 

