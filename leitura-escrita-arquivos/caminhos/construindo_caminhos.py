from pathlib import Path

print(Path.home())
caminho = Path("primeira_pasta/segunda_pasta")

for nome in ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)
    
caminho_absoluto = Path("D:\\projeto\\curso-python-asimov\\leitura-escrita-arquivos\\primeira_pasta\\segunda_pasta\\arquivo1.txt")     
caminho_relativo = Path("primeira_pasta/segunda_pasta/arquivo1.txt")