numero_secreto = 5
descobriu = True


if not descobriu: # condição para verificar se a pessoa não descobriu o número secreto
    numero = int(input("Tente adivinhar o número secreto: ")) # exemplo de entrada do usuário com conversão para número
    if numero < numero_secreto: # condição para verificar se o número digitado é menor que o número secreto
        print("Chute muito baixo!") # mensagem para indicar que o número secreto é maior 
    elif numero > numero_secreto: # condição para verificar se o número digitado é maior que o número secreto
        print("Chute muito alto!") # mensagem para indicar que o número secreto é menor
    else:
        print("Parabéns! Você descobriu o número secreto!") # mensagem para indicar que o número secreto foi descoberto
        descobriu = True # exemplo de atribuição para indicar que a pessoa descobriu o número secreto   
        
if not descobriu: # condição para verificar se a pessoa não descobriu o número secreto
    numero = int(input("Tente adivinhar o número secreto: ")) # exemplo de entrada do usuário com conversão para número
    if numero < numero_secreto: # condição para verificar se o número digitado é menor que o número secreto
        print("Chute muito baixo!") # mensagem para indicar que o número secreto é maior 
    elif numero > numero_secreto: # condição para verificar se o número digitado é maior que o número secreto
        print("Chute muito alto!") # mensagem para indicar que o número secreto é menor
    else:
        print("Parabéns! Você descobriu o número secreto!") # mensagem para indicar que o número secreto foi descoberto
        descobriu = True # exemplo de atribuição para indicar que a pessoa descobriu o número secreto
        
if not descobriu: # condição para verificar se a pessoa não descobriu o número secreto
    numero = int(input("Tente adivinhar o número secreto: ")) # exemplo de entrada do usuário com conversão para número
    if numero < numero_secreto: # condição para verificar se o número digitado é menor que o número secreto
        print("Chute muito baixo!") # mensagem para indicar que o número secreto é maior 
    elif numero > numero_secreto: # condição para verificar se o número digitado é maior que o número secreto
        print("Chute muito alto!") # mensagem para indicar que o número secreto é menor
    else:
        print("Parabéns! Você descobriu o número secreto!") # mensagem para indicar que o número secreto foi descoberto
        descobriu = True # exemplo de atribuição para indicar que a pessoa descobriu o número secreto
        
if descobriu: # condição para verificar se a pessoa descobriu o número secreto
    print("Parabéns! Você completou o jogo!") # mensagem para indicar o fim do jogo 
else:
    print(f"Game Over! Você não conseguiu descobrir o número secreto. O número era {numero_secreto}.") # mensagem para indicar o fim do jogo            