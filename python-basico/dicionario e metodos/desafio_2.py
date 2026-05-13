# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.


estados_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceio",
    "Amapa": "Macapa",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceara": "Fortaleza",
    "Distrito Federal": "Brasilia",
    "Espirito Santo": "Vitoria",
    "Goias": "Goiania",
    "Maranhao": "Sao Luiz",
    "Mato Grosso": "Cuiaba",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Para": "Belém",
    "Paraiba": "Joao Pessoa",
    "Parana": "Curitiba",
    "Pernambuco": "Recife",
    "Piaui": "Teresina",
    "Roraima": "Boa Vista",
    "Rondonia": "Porto Velho",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Sul": "Porto Alegre",
    "Rio Grande do Norte": "Natal",
    "Santa Catarina": "Florianopolis",
    "Sao Paulo": "Sao Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas",
}
resposta_usuario = {}
# for estado, capital in estados_capitais.items():
#     resposta = input(f"\n -> Qual a capital do Estado {estado}?\nEscreva sem acentos: ")
#     resposta_usuario[estado]=resposta
#     saida = input("Deseja continuar?\nDigite \"n\" para sair e \"s\" para continuar !") == "n"
#     if saida:
#         break

# acertos = 0
# for estado, capital in resposta_usuario.items():
#     if capital.lower() == estados_capitais[estado].lower():
#         acertos +=1

# print(f"Você acertou {acertos} de {len(resposta_usuario)} perguntas feitas, isso é {acertos/len(resposta_usuario)*100}%")


# acertos = 0
# for estado, capital in estados_capitais.items():
#     resposta = input(f"\n -> Qual a capital do Estado {estado}?\nEscreva sem acentos: ")
#     if resposta.lower() == capital.lower():
#         acertos +=1
#         print("Resposta Correta!")
#     else:
#         print(f"Resposta errada! O correto seria {capital}")
#     saida = input("Deseja continuar?\nDigite \"n\" para sair e \"s\" para continuar !") == "n"
#     if saida:
#         break
# print(f"Você acertou {acertos} de {len(resposta_usuario)} perguntas feitas, isso é {acertos/len(resposta_usuario)*100}%")


acertos = 0
perguntas_feitas = 0
quer_continuar = True
for estado, capital in estados_capitais.items():
    if not quer_continuar:
        break
    resposta = input(f"\n -> Qual a capital do Estado {estado}?\nEscreva sem acentos: ")
    if resposta.lower() == capital.lower():
        acertos += 1
        print("Resposta Correta!")
    else:
        print(f"Resposta errada! O correto seria {capital}")
    perguntas_feitas += 1
    while True:
        opcao = input("Deseja continuar?\n(s/n)!").lower()
        if opcao not in ["s", "n"]:
            print("Responda apenas com 's' para sim ou 'n' para não.")
            continue
        elif opcao == "n":
            quer_continuar = False
        break
print(
    f"Você acertou {acertos} de {perguntas_feitas} perguntas feitas, isso é {(acertos/perguntas_feitas*100):.2f}%"
)
