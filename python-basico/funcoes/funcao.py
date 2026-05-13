def somar_dois(n):  # n é o parametro que a função recebe
    return n + 2


print(somar_dois(10))  # 10 sendo passado como argumento


def adicionar_final(
    texto, final="!!!"
):  # parametro com valor padrão precisa vir após os parametros sem valor padrão
    return texto + final


print(adicionar_final("olá", "!"))
print(adicionar_final("olá"))


def dividir(a, b):
    if b == 0:
        return "Impossível de dividir!"
    return a / b


print(
    dividir(b=10, a=5)
)  # É possivel explicitar os paramentros que estou passando, se não explicitar o python pega na ordem colocada


def funcao_complexa(valor_1=0, valor_2=0, valor_3=0, valor_4=0): # Função com parametros padrão, que não necessitam que seja passados todos os argumentos
    return valor_1 + valor_2 + valor_3 + valor_4

print(funcao_complexa(valor_3=10))

def funcao_sem_parametro(): # Tem como criar uma função sem parametro / FUNÇÕES SEM RETORNO RETORNARAM NONE(VALOR NULO)
    print("Olá!") # tem como criar função sem retorno
  
funcao_sem_parametro() 
print(funcao_sem_parametro())#retorna um None   