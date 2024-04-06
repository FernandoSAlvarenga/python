#2Interseção de conjuntos:
#Escreva um programa que encontre a interseção de dois conjuntos. Utilize for para iterar pelos elementos e if para verificar a presença em ambos os conjuntos.

conjunto1 = {"a", "b", "c"}
conjunto2 = {"b", "c", "d"}

intersecao = set()

for elemento in conjunto1:
  if elemento in conjunto2:
    intersecao.add(elemento)
print(f"Interseção: {intersecao}")