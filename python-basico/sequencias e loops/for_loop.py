for n in range(10):
    print(f"O valor de n é: {n}")
    
valores = [10, 20, 30, 40, 50]
for valor in valores:   
    print(f"O valor é: {valor}")

nome = "Maria Clara"
for caractere in nome:
    print(f"O caractere é: {caractere}")
    
    
clientes = [("Ana", "xxx", "xxx@email.com"), ("João", "yyy", "yyy@email.com")]    
# for cliente in clientes:
#     nome, telefone, email = cliente
for nome, telefone, email in clientes: # exemplo de desempacotamento de tupla para obter os valores de nome, telefone e email
    print(f"Nome: {nome}, Telefone: {telefone}, Email: {email}\n\n")        
    
   
for n in range(-5, 6):
    print(n)
    if n==0:
        print("O valor de n é igual a 0!") # mensagem para indicar que o valor de n é igual a 0
        continue # exemplo de comando para pular a iteração do loop caso o valor de n seja igual a 0
    resultado =1/n
    print(f"O resultado de 1/{n} é: {resultado}")
print("O loop acabou!") # mensagem para indicar o fim do loop
    
    
    
# numero_secreto = 5
# descobriu = False
# for _ in range(3):
#     if not descobriu: # condição para verificar se a pessoa não descobriu o número secreto
#         numero = int(input("Tente adivinhar o número secreto: ")) # exemplo de entrada do usuário com conversão para número
#         if numero < numero_secreto: # condição para verificar se o número digitado é menor que o número secreto
#             print("Chute muito baixo!") # mensagem para indicar que o número secreto é maior 
#         elif numero > numero_secreto: # condição para verificar se o número digitado é maior que o número secreto
#             print("Chute muito alto!") # mensagem para indicar que o número secreto é menor
#         else:
#             print("Parabéns! Você descobriu o número secreto!") # mensagem para indicar que o número secreto foi descoberto
#             descobriu = True # exemplo de atribuição para indicar que a pessoa descobriu o número secreto 
#             _ = 2 # exemplo de atribuição para interromper o loop caso a pessoa descubra o número secreto  
        
# if descobriu: # condição para verificar se a pessoa descobriu o número secreto
#     print("Parabéns! Você completou o jogo!") # mensagem para indicar o fim do jogo 
# else:
#     print(f"Game Over! Você não conseguiu descobrir o número secreto. O número era {numero_secreto}.") # mensagem para indicar o fim do jogo   