x = 4.5
print(x.as_integer_ratio()) # método para obter a representação fracionária de um número de ponto flutuante, retornando uma tupla com o numerador e denominador da fração equivalente ao número
print(x.is_integer()) # método para verificar se um número de ponto flutuante é um inteiro, retornando True ou False
x=4.0
print(x.is_integer()) # método para verificar se um número de ponto flutuante é um inteiro, retornando True ou False
y =4.9
print(int(y)) # função para converter um número de ponto flutuante em um inteiro, truncando a parte decimal

# STRINGS

texto = "Olá, MunDo!"
print(texto.lower()) # método para converter todos os caracteres de uma string para minúsculas
print(texto.upper()) # método para converter todos os caracteres de uma string para maiúsculas

arquivo = "2026_05_15_NotaFiscal.pdf"
print(arquivo.endswith(".pdf")) # método para verificar se uma string termina com um sufixo específico, retornando True ou False
print(arquivo.startswith("2026")) # método para verificar se uma string começa com um prefixo específico, retornando True ou False

frase = "Python é uma linguagem de programação incrível, e eu adoro aprender python! Python é minha linguagem favorita."
print(frase.count("a")) # método para contar o número de ocorrências de um caractere ou substring em uma string
print(frase.count("Python")) # método para contar o número de ocorrências de um caractere ou substring em uma string
print(frase.lower().count("python")) # método para contar o número de ocorrências de um caractere ou substring em uma string, ignorando diferenças de maiúsculas e minúsculas

seq = "aaaaaaaaaaaaaaaaaabbbaaab"
print(seq.find("b")) # método para encontrar a posição da primeira ocorrência de uma substring em uma string, retornando o índice ou -1 se não for encontrada
print(seq.index("b")) # método para encontrar a posição da primeira ocorrência de uma substring em uma string, retornando o índice ou lançando um erro se não for encontrada
print(seq.find("c")) # método para encontrar a posição da primeira ocorrência de uma substring em uma string, retornando o índice ou -1 se não for encontrada
# print(seq.index("c")) # método para encontrar a posição da primeira ocorrência de uma substring em uma string, retornando o índice ou lançando um erro se não for encontrada 
print(seq[seq.find("b"):]) # acessando o caractere na posição encontrada pela função find

s1 = "13199642446162897"
print(s1.isdigit()) # método para verificar se todos os caracteres de uma string são dígitos, retornando True ou False

s2 = "1234abc5678"
print(s2.isdigit()) # método para verificar se todos os caracteres de uma string são dígitos, retornando True ou False
print(s2.isalpha()) # método para verificar se todos os caracteres de uma string são letras, retornando True ou False
print(seq.isalpha()) # método para verificar se todos os caracteres de uma string são letras, retornando True ou False

frase2 = "   Estou estudando Python!   "
print(frase2.replace("!", "?")) # método para substituir todas as ocorrências de uma substring por outra em uma string
print(frase2.replace("Python", "javaScript")) # método para substituir todas as ocorrências de uma substring por outra em uma string
print(frase2.strip()) # método para remover os espaços em branco do início e do final de uma string
print(frase2.lstrip()) # método para remover os espaços em branco do início de uma string
print(frase2.rstrip()) # método para remover os espaços em branco do final de uma string

frase3 = "Python é uma linguagem de programação incrível,\n\n\n e eu adoro aprender python!\n\n\n Python é minha linguagem favorita."
print(frase3.replace("\n", "")) # método para substituir todas as ocorrências de uma substring por outra em uma string, neste caso, substituindo quebras de linha por caracteres vazios  
print(frase3.replace("\n","").replace(" ", "")) # método para substituir todas as ocorrências de uma substring por outra em uma string, neste caso, substituindo quebras de linha e espaços por caracteres vazios

linha = "item1             item2                        item3"
linha2 = "item1;item2;item3"
print(linha.split()) # método para dividir uma string em uma lista de substrings com base em um delimitador, neste caso, usando o espaço como delimitador padrão, o que resulta em uma lista de palavras sem os espaços extras
print(linha2.split(";")) # método para dividir uma string em uma lista de substrings com base em um delimitador, neste caso, usando o ponto e vírgula como delimitador, o que resulta em uma lista de palavras sem os espaços extras

nomes = ["Maria", "João", "Ana", "Pedro"]
print(" ------ ".join(nomes)) # método para concatenar uma lista de strings em uma única string, usando um delimitador específico, neste caso, usando "------" como delimitador entre os nomes
