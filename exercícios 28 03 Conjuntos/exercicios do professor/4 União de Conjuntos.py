#04União de conjuntos:
#Escreva um programa que encontre a união de dois conjuntos. Utilize for para iterar pelos elementos de ambos os conjuntos e adicionar à lista final.

conjunto1 = {"a", "b", "c"}
conjunto2 = {"b", "c", "d"}

uniao = set()

for elemento in conjunto1:
  uniao.add(elemento)

for elemento in conjunto2:
  uniao.add(elemento)

print(f"União: {uniao}")


