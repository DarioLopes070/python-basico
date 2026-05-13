# ---------------- IMPORTANDO TUDO -----------------
# import modulo

# retorno = modulo.minha_funcao()
# print(retorno)
# print(modulo.x)


# ---------------- IMPORTANDO AS FUNÇÕES ESPECIFICAS PELO NOME ----------------
# from modulo import minha_funcao, x
# from modulo import * # representa a mesma coisa que a linha de cima, o * vai importar todas as variaveis e funções com os nomes originais de dentro do modulo.

# retorno = minha_funcao()
# print(retorno)
# print(x)

# ----------------- IMPORTANDO TUDO, MAS PASSANDO UM APELIDO PARA A BIBLIOTECA OU MODULO ------------------
# import modulo as mm

# retorno = mm.minha_funcao()
# print(retorno)
# print(mm.x)

from modulo import minha_funcao as mf, x as xx

retorno = mf()
print(retorno)
print(xx)