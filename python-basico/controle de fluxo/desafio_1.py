usuario_correto = "pedro"
senha_correta = "senha secreta"

# usuario = input("Digite o nome de usuário: ") # exemplo de entrada do usuário
# senha = input("Digite a senha: ") # exemplo de entrada do usuário

# if usuario == usuario_correto: # condição para verificar se o usuário e a senha estão corretos
#     if senha == senha_correta:
#         print(f"Acesso liberado, seja bem-vindo {usuario}!") # mensagem de sucesso para login
#     else:
#         print(f"Senha incorreta para o usuário {usuario}.") # mensagem de erro para senha incorreta    
# else:
#     print(f"Usuário {usuario} não encontrado.") 
    
    
# USANDO OPERADORES BOOLEANOS PARA VERIFICAR SE O USUÁRIO E A SENHA ESTÃO CORRETOS
usuario = input("Digite o nome de usuário: ") # exemplo de entrada do usuário e comparação direta com o valor correto
usuario_esta_correto = usuario == usuario_correto # exemplo de entrada do usuário e comparação direta com o valor correto
senha_esta_correta = input("Digite a senha: ") == senha_correta # exemplo de entrada do usuário e comparação direta com o valor correto
 
if usuario_esta_correto and senha_esta_correta:
    print(f"Acesso liberado, seja bem-vindo {usuario}!") # mensagem de sucesso para login
elif usuario_esta_correto and not senha_esta_correta:        
    print(f"Senha incorreta para o usuário {usuario}.") # mensagem de erro para senha incorreta
else:
    print(f"Usuário {usuario} não encontrado.")                
    
