# from moduloA.script_A import var_A # RODA PARA QUEM ESTÁ DENTRO DA PASTA "exemplo_importacao"
# from moduloB.script_B import var_B # RODA PARA QUEM ESTÁ DENTRO DA PASTA "exemplo_importacao"
# from moduloC.script_C import var_C # RODA PARA QUEM ESTÁ DENTRO DA PASTA "exemplo_importacao"
from exemplo_importacao.moduloA.script_A import var_A # RODA PARA QUEM ESTÁ DENTRO DA PASTA "estruturacao de projeto"
from exemplo_importacao.moduloB.script_B import var_B # RODA PARA QUEM ESTÁ DENTRO DA PASTA "estruturacao de projeto"
from exemplo_importacao.moduloC.script_C import var_C # RODA PARA QUEM ESTÁ DENTRO DA PASTA "estruturacao de projeto"

def func():
    print(var_A + var_B + var_C)
    
    
if __name__ == "__main__":
    print("Testando: func")    
    func()