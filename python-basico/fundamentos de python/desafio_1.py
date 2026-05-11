nome = input("Qual o seu nome?\nDigite aqui: ") # exemplo de entrada do usuário
idade = int(input("Qual a sua idade?\nDigite aqui: ")) # exemplo de entrada do usuário com conversão para número

# USANDO FUNÇÃO DIRETO NA HORA DE PRINTAR
# print("Olá, " + nome + "! Bem-vindo ao curso de Python!") # exemplo
# print("Seu nome tem " + str(len(nome)) + " caracteres.") # exemplo de entrada do usuário com operação matemática
# print("Em 5 anos, você terá " + str(idade + 5) + " anos.") # exemplo de entrada do usuário com operação matemática

# USANDO VARIÁVEIS PARA GUARDAR O RESULTADO DAS OPERAÇÕES
# print("Olá, " + nome + "! Bem-vindo ao curso de Python!") # exemplo
# caracteres_nome = len(nome) # cálculo do número de caracteres no nome
# print("Seu nome tem {caracteres} caracteres.".format(caracteres=caracteres_nome)) # exemplo de entrada do usuário com operação matemática
# idade_futura = idade + 5 # cálculo da idade futura
# print("Em 5 anos, você terá {idade} anos.".format(idade=idade_futura)) # exemplo de entrada do usuário com operação matemática

# USANDO F-STRINGS PARA FORMATAR AS MENSAGENS
print('-'*10) # linha de separação
print(f"Olá, {nome}! Bem-vindo ao curso de Python!") # exemplo
print(f"Seu nome tem {len(nome)} caracteres.") # exemplo de entrada do usuário com operação matemática
print(f"Em 5 anos, você terá {idade + 5} anos.") # exemplo de entrada do usuário com operação matemática
print('-'*15) # linha de separação