pessoas = ["Dário", "Maria", "João", "Ana", "Carlos"] # exemplo de lista com nomes de pessoas
print(pessoas[1:4]) # exemplo de slicing para obter os elementos do índice 1 ao 3 (exclusivo)
print(pessoas[2:3]) # exemplo de slicing para obter o elemento do índice 2
len(pessoas) # exemplo de uso da função len() para obter o número de elementos na lista
print(pessoas[1:]) # exemplo de slicing para obter os elementos a partir do índice 1 até o final da lista
print(pessoas[:-1]) # exemplo de slicing para obter os primeiros 4 elementos da lista
print(pessoas[:]) # exemplo de slicing para obter todos os elementos da lista (cria uma cópia da lista)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # exemplo de lista com números
print(numeros[::2]) # exemplo de slicing para obter os elementos com passo 2
print(numeros[1::2]) # exemplo de slicing para obter os elementos do índice 1 ao 9 (exclusivo) com passo 2
print(numeros[::-1]) # exemplo de slicing para obter os elementos do índice -1 ao 0 (exclusivo) com passo 2
print(numeros[::-2]) # exemplo de slicing para obter os elementos do índice -1 ao 1 (exclusivo) com passo 2
print(numeros[-2::-2]) # exemplo de slicing para obter os elementos do índice -2 ao 0 (exclusivo) com passo 2