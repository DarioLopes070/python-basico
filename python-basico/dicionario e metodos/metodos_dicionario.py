produtos = {"caneta": 2.50, "caderno": 15.00, "lapis": 1.00}
print(produtos) 
# produtos.clear() # método para limpar o dicionário, removendo todos os itens
# print(produtos)

print(produtos.get("caneta")) # método para obter o valor associado a uma chave específica, retornando None se a chave não existir
print(produtos.get("borracha", "Produto não encontrado")) # método para obter o valor associado a uma chave específica, retornando uma mensagem personalizada se a chave não existir
produtos.setdefault("borracha", 0.50) # método para obter o valor associado a uma chave específica, ou definir um valor padrão se a chave não existir
print(produtos)
for produto in produtos.keys(): # método para obter uma lista das chaves do dicionário
    print(produto)
for valor in produtos.values(): # método para obter uma lista dos valores do dicionário
    print(valor)
# for itens in produtos.items(): # método para obter uma lista de tuplas contendo as chaves e valores do dicionário
    # print(itens)        
for k, v in produtos.items(): # método para obter uma lista de tuplas contendo as chaves e valores do dicionário, usando desempacotamento de tuplas
    print(f"Produto: {k} -> Preço: {v}")
    
novos_produtos = {"mochila": 50.00, "garrafa": 20.00, "caderno": 12.00}
print(produtos)
produtos.update(novos_produtos) # método para atualizar o dicionário com os itens de outro dicionário, sobrescrevendo os valores das chaves existentes
print(produtos)

produtos_copia = produtos.copy() # método para criar uma cópia do dicionário
produtos_copia["grampeador"] = 3.00 # adicionando um novo item à cópia do dicionário
print(produtos) # o dicionário original permanece inalterado
print(produtos_copia) # a cópia do dicionário contém o novo item adicionado