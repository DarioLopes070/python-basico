# arquivo para exemplificar a estruturação correta dentro de um projeto com varias pastas:
# 1 - Criar ambiente virtual na pasta raiz do projeto
# python -m venv venv -> criar o venv
# venv/scripts/activate - ativar venv
# 2 - instalar biblioteca setuptools 
# pip install setuptools
# 3 - adicionar um arquivo __init__.py em branco dentro da pasta abaixo da raiz que deseja acessar
# 4 - criar arquivo setup.py com as configurações em questão
# 5 - Rodar o comando: pip install -e .


from exemplo_importacao.meu_codigo import func

func()