# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum()!
# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !
# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero
media = soma / len(numeros)
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")

maior = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
print(f"O maior número é: {maior}")

palavras = ["casa", "carro", "bicicleta", "avião", "computador"]
for palavra in palavras:
    if len(palavra) >= 5:
        print(f"A palavra '{palavra}' tem pelo menos 5 caracteres.")
