idade = int(input("Digite a sua idade: ")) # exemplo de entrada do usuário com conversão para número
if idade < 18: # condição para verificar se a idade é menor que 18
    print("Você é menor de idade.") # mensagem para menores de idade
elif idade == 18: # condição para verificar se a idade é igual a 18
    print("Você tem exatamente 18 anos.") # mensagem para quem tem exatamente 18 anos
else:
    print("Você tem mais de 18 anos .") # mensagem para maiores de idade