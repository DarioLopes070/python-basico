from pathlib import Path
import os


# Listando arquivos de uma pasta
# print(os.listdir(Path.cwd()))
visitados = set()
def pesquisar_diretorio(diretorio=(Path.home() / "Documents").glob("*")):
    for arquivo in diretorio.glob("*"):
        if arquivo.exists() and arquivo not in visitados:
            print(f"--------Nome do arquivo: {arquivo.name} --> {os.path.getsize(arquivo)}")
            if arquivo.is_dir() and any(arquivo.glob("*")):
                return arquivo
            else:
                visitados.add(arquivo)
                
    visitados.add(arquivo.parent)
    return arquivo.parent.parent        
    
# for arquivo in (Path.home() / "Documents").glob("*"):
for arquivo_pai in (Path("D:\\dario") / "Documents").glob("*"):
    # print(list(Path.cwd().glob("*")))
    ainda_tem_arquivo = True
    if arquivo_pai.exists():
        print(f"Nome do arquivo: {arquivo_pai.name} -----> {os.path.getsize(arquivo_pai)}")
        if arquivo_pai.is_dir() and any(arquivo_pai.glob("*")):
            arquivo = arquivo_pai
            while True:
                if arquivo_pai.parent not in arquivo.parents:
                    break 
                if arquivo not in visitados:
                    arquivo = pesquisar_diretorio(arquivo)
                else:    
                    arquivo = arquivo.parent    
            # for arquivo_dentro in arquivo.glob("*"):
            #     if arquivo_dentro.exists():
            #         print(f"Nome do arquivo: {arquivo_dentro.name} --> {os.path.getsize(arquivo_dentro)}")
                        
                        

# # Listando arquivos de uma determinada extensão dentro de uma pasta
# print(list(Path.cwd().glob("*.py")))


# # Listando tudo dentro de uma pasta
# print(list(Path.cwd().glob("**/*")))
# print(list(Path.cwd().glob("**/*.txt")))


# # Validando caminhos
# print(Path.home().exists())
# nao_existe = Path.home() / "nao_existe"
# print(nao_existe.exists())

# Verificando se é arquivo ou pasta
# print(Path(__file__))
# print(Path(__file__).is_file())
# print(Path(__file__).parent)
# print(Path(__file__).parent.is_file())
# print(Path(__file__).parent.is_dir())