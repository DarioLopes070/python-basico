from pathlib import Path
import os


# def retornar_tamanho_dos_diretorios(caminho, profundidade=1):
#     for arquivo in caminho.glob("*"):
#         print(f"{arquivo.name} ---> {os.path.getsize(arquivo)}")


# caminho = Path.home() / "Documents"
# # os.path.getsize(arquivo) ---> pegar tamanho do arquivo
# retornar_tamanho_dos_diretorios(caminho, profundidade=1)


visitados = set()
tamanho = {}
def pesquisar_diretorio(diretorio=(Path.home() / "Documents").glob("*")):
    for arquivo in diretorio.glob("*"):
        if arquivo.exists() and arquivo not in visitados:
            print(f"--------Nome do arquivo: {arquivo.name} --> {os.path.getsize(arquivo)}")
            if arquivo.is_file():
                tamanho[arquivo] = os.path.getsize(arquivo)
            if arquivo.is_dir() and any(arquivo.glob("*")):
                return arquivo
            else:
                visitados.add(arquivo)
                
    visitados.add(arquivo.parent)
    return arquivo.parent.parent  

def calcular_tamanho(tamanho, caminho_raiz):
    tamanho_final = {}
    for arquivo, tamanho_arquivo in tamanho.items():
        while caminho_raiz in arquivo.parents or caminho_raiz == arquivo:
            if arquivo.parent in tamanho_final or caminho_raiz == arquivo:
                if arquivo != caminho_raiz:
                    tamanho_final[arquivo.parent] += tamanho_arquivo 
                else:
                    tamanho_final[arquivo] += tamanho_arquivo                      
            else:
                if arquivo != caminho_raiz:
                    tamanho_final[arquivo.parent] = tamanho_arquivo
                else:
                    tamanho_final[arquivo] = tamanho_arquivo 
            arquivo = arquivo.parent      
    return tamanho_final              
    
# for arquivo in (Path.home() / "Documents").glob("*"):
for arquivo_pai in (Path("D:\\dario") / "Documents").glob("*"):
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
                    
print("\n\n\n\n\n\n\n")                    
tamanho_calculado = calcular_tamanho(tamanho,(Path("D:\\dario") / "Documents"))
for key, value in tamanho_calculado.items():
    print(f"Arquivo: {key} -----> Tamanho: {value/(1024*1024)}MB")