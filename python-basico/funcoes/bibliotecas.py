# --------------------- BIBLIOTECA DATETIME ----------------------
# import datetime

# agora = datetime.datetime.now()

# ano_2000 = datetime.datetime(2000,1,1)

# print(agora - ano_2000)

# --------------------- BIBLIOTECA RANDOM ------------------------
# import random

# for _ in range(5):
#     n = random.randint(1, 10)
#     print(f"Número escolhido: {n}")

# nomes = ["Dário", "Maria", "João", "Jesus"]
# for _ in range(5):
#     nome  = random.choice(nomes)    
#     print(f"Nome escolhido: {nome}")

# --------------------- BIBLIOTECA OS ------------------------
# import os
# print(os.getcwd())
# print(os.listdir())

# --------------------- BIBLIOTECA TIME ------------------------
import time
inicio = time.time()
print("Primeira linha")
time.sleep(1)
print("Segunda linha")
final = time.time()

tempo_execucao = final - inicio
print(f"O script levou {tempo_execucao:.5f} segundos para executar")