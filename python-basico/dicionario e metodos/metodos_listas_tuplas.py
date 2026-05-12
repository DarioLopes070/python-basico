tup = (0, 0, 0, 0, 0, 1, 1, 1, 1, 1)
print(tup.index(1)) # método para encontrar a posição da primeira ocorrência de um elemento em uma tupla, retornando o índice ou lançando um erro se não for encontrado
print(tup.count(0)) # método para contar o número de ocorrências de um elemento em uma tupla, retornando o número de vezes que o elemento aparece   
l1 = [0, 0, 1 , 0, 1, 0, 0]
l2 = l1.copy() # método para criar uma cópia de uma lista, retornando uma nova lista com os mesmos elementos
print(l1) # lista original
print(l2) # nova lista criada a partir da cópia da lista original
l1.clear() # método para remover todos os elementos de uma lista, deixando-a vazia
print(l1) # lista original após ser limpa
print(l2) # nova lista permanece inalterada após a limpeza da lista original

for n in range(5):
    l1.append(n*2)
print(l1) # lista original após adicionar elementos usando o método append, que adiciona um elemento ao final da lista
l1.append("hello") # método para adicionar um elemento ao final de uma lista, neste caso, adicionando a string "hello" à lista
print(l1) # lista original após adicionar a string "hello" usando o método append
valores = [10, 20, 30, -40, -10, 0, 1]
valores_positivos = []
for v in valores:
    if v >0:
        valores_positivos.append(v) # método para adicionar um elemento ao final de uma lista, neste caso, adicionando apenas os valores positivos da lista original à nova lista
print(valores_positivos) # nova lista contendo apenas os valores positivos da lista original
valores.extend(valores_positivos) # método para adicionar os elementos de uma lista a outra lista, neste caso, adicionando os valores positivos da lista original à lista original
print(valores) # lista original após adicionar os valores positivos usando o método extend, que adicion

numeros = [1, 2, 3, 4, 5]
numeros_novos = numeros + [6, 7, 8] # operador de concatenação para criar uma nova lista combinando os elementos da lista original com novos elementos
print(numeros) # lista original permanece inalterada após a concatenação
print(numeros_novos) # nova lista criada a partir da concatenação da lista original com novos elementos

vogais = ['a', 'i', 'o', 'u']    
print(vogais) # lista original após a inserção da vogal 'e' usando o método insert, que insere um elemento em uma posição específica da lista
print(vogais.insert(1, 'e')) # método para inserir um elemento em uma posição específica de uma lista, neste caso, inserindo a vogal 'e' na posição 1 da lista

valores = [10, 20, 30, -40, -10, 0, 1]
valor_removido = valores.pop() # método para remover e retornar o último elemento de uma lista, neste caso, removendo o valor 1 da lista original
print(valores) # lista original após a remoção do último elemento usando o método pop
print(valor_removido) # valor removido da lista original usando o método pop
valor_removido = valores.pop(0) # método para remover e retornar um elemento em uma posição específica de uma lista, neste caso, removendo o valor 10 da posição 0 da lista original
print(valores) # lista original após a remoção do elemento na posição 0 usando o método pop
print(valor_removido) # valor removido da lista original usando o método pop

clientes = ["Maria", "João", "Ana", "Pedro"]
while clientes:
    cliente = clientes.pop() # método para remover e retornar o último elemento de uma lista, neste caso, removendo os clientes da lista original um por um até que a lista fique vazia
    print(f"Atendendo cliente: {cliente}") # imprimindo o nome do cliente atendido a cada iteração do loop, mostrando o processo de atendimento dos clientes da lista original
print(clientes) # lista original após atender todos os clientes usando o método pop, resultando em uma lista vazia  

print(valores.reverse()) # método para inverter a ordem dos elementos de uma lista, modificando a lista original
print(valores.sort()) # método para ordenar os elementos de uma lista em ordem crescente, modificando a lista original
