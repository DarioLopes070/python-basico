# print(True and True) # operador lógico AND, retorna True se ambos os operandos forem True, caso contrário, retorna False
# print(True and False) # operador lógico AND, retorna True se ambos os operandos forem True, caso contrário, retorna False
# print(False and True) # operador lógico AND, retorna True se ambos os operandos forem True  , caso contrário, retorna False
# print(False and False) # operador lógico AND, retorna True se ambos os operandos forem True, caso contrário, retorna False
# print("\n") 
# print(True or True) # operador lógico OR, retorna True se pelo menos um dos operandos for True, caso contrário, retorna False       
# print(True or False) # operador lógico OR, retorna True se pelo menos um dos operandos for True, caso contrário, retorna False
# print(False or True) # operador lógico OR, retorna True se pelo menos um dos operandos for True, caso contrário, retorna False
# print(False or False) # operador lógico OR, retorna True se pelo menos um dos operandos for True, caso contrário, retorna False
# print("\n")
# print(not True) # operador lógico NOT, retorna False se o operando for True, caso contrário, retorna True
# print(not False) # operador lógico NOT, retorna False se o operando for True, caso contrário, retorna True


print("---- INICIO ----\n")
estou_com_fome = input("Está com fome? (Digite s para sim): ") == 's' # exemplo de variável booleana
tenho_comida = input("Você tem comida em casa? (Digite s para sim): ") == 's' # exemplo de variável booleana
if estou_com_fome and not tenho_comida: # condição para verificar se a pessoa está com fome e não tem comida em casa
    print("Ir ao mercado")    
    print("Voltar para casa")
    print("Preparar Refeição")
    print("Comer a comida")
if estou_com_fome and tenho_comida: # condição para verificar se a pessoa está com fome e tem comida em casa
    print("Preparar Refeição")
    print("Comer a comida")    
print("\n---- FIM ----")