from pathlib import Path
import shutil

'''
# Criando pastas 
pasta_atual = Path(__file__).parent
# caminho_pasta_destino = pasta_atual / "destino4"
# caminho_pasta_destino.mkdir(exist_ok=True) # Cria pasta se ela não existir, caso contrário, não faz nada
caminho_pasta_destino = pasta_atual / "destino5" / "destino51"
caminho_pasta_destino.mkdir(parents=True) # Cria pasta e subpastas, caso elas não existam, caso contrário, não faz nada
'''

'''
# Copiando pastas 
pasta_atual = Path(__file__).parent
pasta_copiada = pasta_atual / "destino5"
pasta_destino = pasta_destino = pasta_atual / "destino1" / "destino5"
shutil.copytree(pasta_copiada,  pasta_destino)
'''

'''
# Deletando pastas  vazias
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / "destino1"
pasta_remover.rmdir() # só remove pastas vazias, caso contrário, levanta um erro
'''

# Deletando pastas com conteudos
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / "destino1"
shutil.rmtree(pasta_remover) # remove pasta e todo o seu conteúdo, caso contrário, levanta um erro