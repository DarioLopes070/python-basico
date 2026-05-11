# print(4==4) # operador de comparação de igualdade, retorna True se os valores forem iguais, caso contrário, retorna False
# print(4!=4) # operador de comparação de desigualdade, retorna True se os valores forem diferentes, caso contrário, retorna False
# print(4>4)  # operador de comparação de maior que, retorna True se o valor da esquerda for maior que o valor da direita, caso contrário, retorna False
# print(4<4) # operador de comparação de menor que, retorna True se o valor da esquerda for menor que o valor da direita, caso contrário, retorna False
# print(4>=4) # operador de comparação de maior ou igual, retorna True se o valor da esquerda for maior ou igual ao valor da direita, caso contrário, retorna False
# print(4<=4) # operador de comparação de menor ou igual, retorna True se o valor da esquerda for menor ou igual ao valor da direita, caso contrário, retorna False

print("---- INICIO ----\n")
fome = input("Está com fome? (Digite s para sim): ") # exemplo de variável booleana
if fome == 's': # condição para verificar se a pessoa está com fome
    comida_em_casa = input("Você tem comida em casa? (Digite s para sim): ") # exemplo de variável booleana
    if comida_em_casa != 's': # condição para verificar se a pessoa não tem comida em casa
        print("Ir ao mercado")    
        print("Voltar para casa")    
    print("Preparar Refeição")
    print("Comer a comida")
print("\n---- FIM ----")    
    
    