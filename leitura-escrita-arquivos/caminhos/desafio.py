from pathlib import Path
import os

# def retornar_tamanho_dos_diretorios(caminho, profundidade=1):
#     for arquivo in caminho.glob("*"):
#         print(f"{arquivo.name} ---> {os.path.getsize(arquivo)}")


# caminho = Path.home() / "Documents"
# # os.path.getsize(arquivo) ---> pegar tamanho do arquivo
# retornar_tamanho_dos_diretorios(caminho, profundidade=1)


# Código para montar a hierarquia de pastas e arquivos
def montar_arvore(pasta, hierarquia):
    try:
        lista_arquivos = os.listdir(pasta)
    except PermissionError:
        return    
    if not hierarquia:
        hierarquia.setdefault(pasta.name, {})
    for arquivo in lista_arquivos:
        arquivo = Path(Path.cwd() / pasta / arquivo)
        nome_pasta = pasta.name
        if arquivo.is_file():
            nome_arquivo = arquivo.name
            tamanho_arquivo = os.path.getsize(arquivo)
            hierarquia.setdefault(nome_pasta, {}).setdefault(
                nome_arquivo, {}
            ).setdefault("tamanho", tamanho_arquivo)
            hierarquia.setdefault(nome_pasta, {}).setdefault(
                nome_arquivo, {}
            ).setdefault("tipo", "arquivo")
        elif arquivo.is_dir():
            montar_arvore(
                Path.cwd() / pasta / arquivo, hierarquia.setdefault(nome_pasta, {})
            )


# Código para Calcular tamanho das de pastas
def calcular_tamanho(hierarquia):
    soma_tamanho = 0

    for nome, conteudo in hierarquia.items():
        if nome == "tamanho":
            continue
        if conteudo.get("tipo") == "arquivo":
            soma_tamanho += hierarquia[nome]["tamanho"]
        else:
            soma_tamanho += calcular_tamanho(hierarquia[nome])
    hierarquia.setdefault("tamanho", soma_tamanho)
    return soma_tamanho


# Código para Calcular tamanho das de pastas
def exibir_arvore(hierarquia, nivel=0, profundidade=0, prefixo=""):
    exibir = ""
    if profundidade < nivel:
        return ""
    for nome, conteudo in hierarquia.items():
        if nome == "tamanho" or nome == "tipo":
            continue
        if conteudo.get("tipo") == "arquivo":
            icone = "📄"
        else:
            icone = "📁"
        ultimo_item = [
            chave for chave in hierarquia.keys() if chave not in ["tamanho", "tipo"]
        ][-1]
        eh_ultimo = nome == ultimo_item
        if eh_ultimo:
            conector = "└── "
        else:
            conector = "├── "
        if eh_ultimo:
            novo_prefixo = prefixo + "    "
        else:
            novo_prefixo = prefixo + "│   "

        tamanho = (
            (conteudo.get("tamanho")) / (1024**2) if conteudo.get("tamanho") else 0
        )
        texto_visual = prefixo + conector + icone + " " + nome
        exibir += f"{texto_visual:<100}{tamanho:.2f}MB\n"
        exibir += exibir_arvore(hierarquia[nome], nivel + 1, profundidade, novo_prefixo)
    return exibir


def main(diretorio, profundidade):
    hierarquia = {}
    montar_arvore(diretorio, hierarquia)
    raiz = next(iter(hierarquia))
    calcular_tamanho(hierarquia[raiz])
    exibir = exibir_arvore(hierarquia=hierarquia, profundidade=profundidade)
    print(exibir)
    return exibir

# diretorio = Path("D:\\dario") / "Documents"
diretorio = Path.home() / "Documents"
profundidade = 3
main(diretorio, profundidade)