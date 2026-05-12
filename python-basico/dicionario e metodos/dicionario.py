capitais = {"Brasil": "Brasilia", "Argentina": "Buenos Aires", "França": "Paris"}
capitais["Inglaterra"] = "Londres"
print(capitais)
print(capitais["Brasil"])
del capitais["Argentina"]
print(capitais)

for pais in capitais:
    capital = capitais[pais]
    print(f"A capital do {pais} é {capital}")

d = dict()  # ou d={}

d[10] = "abc"
d["CHAVE"] = 5
d[3.15] = True
for k in d:
    v = d[k]
    print(f"Chave: {k} -> Valor: {v}")

print("Brasil" in capitais)
print("Brasilia" in capitais)

pais = "Japão"
if pais in capitais:
    print(f"A capital do {pais} é {capitais[pais]}")
else:
    print(f"Não já capital cadastrada para o país {pais}")  
    
# USO DE IN

lista = [1, 2, 3, 4, 5]
print(3 in lista)
tupla = (1, 2, 3, 4, 5)      
print(3 in tupla)
texto = "Eu gosto de Python"
print("Python" in texto)
print("python" in texto)