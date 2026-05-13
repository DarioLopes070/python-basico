# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

# ------------------- MINHA SOLUÇÂO --------------------
alfabeto = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
import re


def somente_letras_puras(texto):
    return bool(re.fullmatch(r"[a-zA-Z]+", texto))

def cifrar_texto(letra, alfabeto, chave):
        indice_buscado = alfabeto.index(letra.upper()) + chave
        while indice_buscado >= len(alfabeto):
            indice_buscado -= len(alfabeto)
        while indice_buscado < 0:
            indice_buscado += len(alfabeto) 
        return alfabeto[indice_buscado] if letra.isupper() else alfabeto[indice_buscado].lower()


entrada = input("Digite aqui o que deseja encriptografar: ")
chave = int(input("Digite aqui o valor da chave: "))

cifra = ""
for letra in entrada:
    if not somente_letras_puras(letra):
        cifra += letra
        continue
    cifra += cifrar_texto(letra, alfabeto, chave)
print(cifra)


# -------------------------- SOLUÇÃO PROFESSOR ----------------------------


# def cifrar_caractere(caractere, seq, chave):
#     indice = seq.index(caractere)
#     novo_indice = indice + chave
#     while novo_indice >= len(seq): # corrige se o valor passado for maior que o numeros de letras no alfabeto
#         novo_indice = novo_indice - len(seq)
#     while novo_indice < 0: # corrige se o valor passado for menor que o numeros de letras no alfabeto
#         novo_indice = novo_indice + len(seq)
#     return seq[novo_indice]


# maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# minusculas = "abcdefghijklmnopqrstuvwxyz"

# texto = "ABCDExyz"
# chave = -3
# cifra = ""

# for caractere in texto:
#     if caractere in minusculas:
#         caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
#     elif caractere in maiusculas:
#         caractere_cifra = cifrar_caractere(caractere, maiusculas, chave)
#     else:
#         caractere_cifra = caractere
#     cifra += caractere_cifra

# print(cifra)
