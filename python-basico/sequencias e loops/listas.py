print([1, 2, 3, 4, 5]) # exemplo de lista com números
print(["maçã", "banana", "laranja"]) # exemplo de lista com strings
lista_misturada = [1, "maçã", 3.14, True] # exemplo de lista com diferentes tipos de dados
print(lista_misturada) # exemplo de impressão da lista misturada
print("\n")
lista_com_listas = [[1, 2, 3], ["maçã", "banana", "laranja"], [True, False]] # exemplo de lista contendo outras listas
print(lista_com_listas) # exemplo de impressão da lista contendo outras listas
print([1,"banana", True, 2.4, ["daniel", "ana"]]) # exemplo de lista com diferentes tipos de dados, incluindo outra lista
print("\n")
# exemplo de acesso a elementos da lista usando índices
print(lista_com_listas[0]) # acesso à primeira lista dentro da lista_com_listas
print(lista_com_listas[1]) # acesso à segunda lista dentro da lista_com_listas
print(lista_com_listas[-1][1]) # acesso ao segundo elemento da última lista dentro da lista_com_listas (acesso à string "False") 

# AULA EXTRA PARA LISTAS: Compreensão de lista
valores = list(range(10))
# maiores_que_cinco = []
# for valor in valores:
#     if valor > 5:
#         maiores_que_cinco.append(valores)
maiores_que_cinco = [
    valor   # RESULTADO
    for valor in valores    # para cada ELEMENTO in SEQUÊNCIA 
    if valor > 5    # se CONDIÇÃO
]        
print(valores)
print(maiores_que_cinco)        