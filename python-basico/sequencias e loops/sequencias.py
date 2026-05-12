nome = "Dário" # exemplo de string
print(nome[0]) # exemplo de impressão do primeiro caractere da string
lista = [1,2,3,4,5] # exemplo de lista com números
print(tuple(lista)) # exemplo de conversão da lista para tupla
print(list(tuple(lista))) # exemplo de conversão da tupla de volta para lista
str() # cria uma string vazia
list() # cria uma lista vazia
tuple() # cria uma tupla vazia
bool() # cria um valor booleano False
bool("") # cria um valor booleano False
bool("Hello, World!") # cria um valor booleano True

seq = "Python" # exemplo de string
if seq:
    print("A sequência não está vazia.") # exemplo de impressão se a sequência não estiver vazia
else:
    print("A sequência está vazia.") # exemplo de impressão se a sequência estiver vazia
