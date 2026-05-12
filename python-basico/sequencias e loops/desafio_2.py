# Dado duas listas, printe todos os valores que aparecerem # duplicados nas duas listas.
# Dado duas listas, printe uma mensagem dizendo se existe # algum elemento em comum entre elas ou não.

lista_1 = [1, 2, 3, 4, 5, 1, 2, 7, 8, 9, 10, 3]
lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 9, 10]

for numero in lista_1: 
    for numero_2 in lista_2:
        if numero == numero_2  and numero: # condição para verificar se os números são iguais, os índices são diferentes e o número ainda não foi adicionado à lista de números iguais
            print(f"O número {numero} é semelhante nas duas listas.")

print("\n\n")
lista1 = ["dario", True, "xyz"]
lista2 = ["abc", False, "xyz"]
elemento_comum = False
for elemento in lista1: 
    if elemento_comum:
        break # exemplo de comando para interromper o loop caso seja encontrado um elemento em comum entre as duas listas
    for elemento_2 in lista2:
        if elemento == elemento_2:
            elemento_comum = True
            break # exemplo de comando para interromper o loop caso seja encontrado um elemento em comum entre as duas listas
if not elemento_comum:
    print(f"As listas {lista1} e {lista2} não possuem elementos em comum.")
else:
    print(f"As listas {lista1} e {lista2} possuem elementos em comum.")    