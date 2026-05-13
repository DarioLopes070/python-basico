# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.


# ------------------------- MEU CÓDIGO ------------------------------------
import random

# baralho = []
# def gerar_baralho(qtd=1, coringa=True, embaralhar=True):
#     # baralho = "" # -> gera os valores como uma string
#     baralho_misturado = []
#     # naipes = list("♠♥♦♣")
#     for i in range(qtd):
#         for m in ["♠", "♣", "♥", "♦"]:
#         # for m in naipes:
#             for n in ["A"]:
#                 baralho.append(f"{n}{m}")
#                 # baralho += (f"{n}{m}, ")
#             for n in range(2, 11):
#                 baralho.append(f"{n}{m}")
#                 # baralho += (f"{n}{m}, ")
#             for n in ["J", "Q", "K"]:
#                 baralho.append(f"{n}{m}")
#                 # baralho += (f"{n}{m}, ")
#         if coringa:
#             for _ in range(2):
#                 baralho.append(f"JK{i+1}")
#                 # baralho += (f"JK{i+1}, ")
#         if embaralhar:
#             baralho_misturado = random.shuffle(baralho)
#     return baralho if not baralho_misturado else baralho_misturado


# def mostrar_baralho(baralho_definido):
#     print(f"\n\nHá {len(baralho_definido)} cartas no baralho!")
#     print(f"Cartas:\n{baralho_definido}")

# def dar_as_cartas(baralho_definido, n_jogadores=4, n_cartas=5):
#     cartas_do_jogador = []
#     for jogador in range(n_jogadores):
#         cartas_do_jogador.append([])
#         for cartas in range(n_cartas):
#             cartas_do_jogador[jogador].append(baralho_definido.pop(random.randint(0,len(baralho_definido)-1)))
#     return cartas_do_jogador, baralho_definido    

# def mostrar_jogadores(cartas, n_jogadores=4, n_cartas=5):
#     for jogador in range(n_jogadores):
#         print(f"Há {len(cartas)} cartas na mão do Jogador {jogador+1}\nCartas:")
#         for carta in range(n_cartas):    
#             print(f"- {cartas[jogador][carta]}") 

# baralho_definido = gerar_baralho(2, True, True)
# mostrar_baralho(baralho_definido)
# cartas, baralho_restante = dar_as_cartas(baralho_definido, 5, 5)
# mostrar_baralho(baralho_restante)
# mostrar_jogadores(cartas, 5, 5)


# ------------------------------------ SOLUÇÃO PROFESSOR ------------------------------------------------



def gerar_baralho(n_copias=2, coringa=True, embaralhar=True):
    baralho = []
    naipes = list("♠♥♦♣")
    numeros = list("A23456789") + ["10"] + list("JQK")
    for i in range(n_copias):
        for naipe in naipes:
            for numero in numeros:
                baralho.append(numero+naipe)
        if coringa:
                baralho.extend(["JK1", "JK2"])
        if embaralhar:
            random.shuffle(baralho)
    return baralho


def mostrar_baralho(baralho_definido):
    print(f"\n\nHá {len(baralho_definido)} cartas no baralho!")
    print("Cartas:")
    print(", ".join(baralho_definido))

def dar_as_cartas(baralho_definido, n_jogadores=4, n_cartas=5):
    jogadores = {}
    for jogador in range(n_jogadores):
        mao =[]
        while len(mao) < n_cartas:
            carta = baralho_definido.pop(0)
            mao.append(carta)
        nome_jogador = f"Jogador {jogador+1}" 
        jogadores[nome_jogador] = mao   
    return jogadores    

def mostrar_jogadores(jogadores, n_jogadores=4, n_cartas=5):
    for jogador, mao in jogadores.items():
        print(f"Há {len(mao)} cartas na mão do Jogador {jogador}\nCartas:")
        for carta in mao:    
            print(f"-> {carta}") 

baralho_definido = gerar_baralho()
mostrar_baralho(baralho_definido)
jogadores = dar_as_cartas(baralho_definido, 5, 5)
mostrar_baralho(baralho_definido)
mostrar_jogadores(jogadores, 5, 5)