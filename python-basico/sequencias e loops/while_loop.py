n = 0
while n<10: # condição para verificar se o valor de n é menor que 10
    print(f"O valor de n é: {n}")
    n += 1 # exemplo de incremento para atualizar o valor de n a cada iteração do loop
    if n == 5: # condição para verificar se o valor de n é igual a 5
        print("O valor de n é igual a 5!") # mensagem para indicar que o valor de n é igual a 5
        break # exemplo de comando para interromper o loop caso o valor de n seja igual a 5
print("O loop acabou!") # mensagem para indicar o fim do loop


while True: # exemplo de loop infinito
    entrada = input("Digite algo (ou 's' para encerrar): ") # exemplo de entrada do usuário
    print(f"Você digitou: {entrada}")
    if entrada == 's': # condição para verificar se a entrada do usuário é igual a 's'
        break
print("O loop acabou!") # mensagem para indicar o fim do loop

while True: # exemplo de loop infinito
    opt = input("Escolha uma opção (1, 2) | (s para encerrar): ") # exemplo de entrada do usuário
    if opt == "s": # condição para verificar se a opção escolhida é igual a 's'
        break
    elif opt != "1" and opt != "2": # condição para verificar se a opção escolhida é diferente de '1' e '2'
        print(f"Opção inválida!") # mensagem para indicar que a opção escolhida é inválida
        continue # exemplo de comando para pular a iteração do loop caso a opção escolhida seja inválida 
    print(f"Você escolheu a opção {opt}") # mensagem para indicar a opção escolhida pelo usuário
print("O loop acabou!") # mensagem para indicar o fim do loop    