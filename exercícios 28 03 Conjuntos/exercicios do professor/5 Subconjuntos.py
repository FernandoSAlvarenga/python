#5Subconjuntos:
#Escreva um programa que determine se um conjunto é subconjunto de outro. Utilize for para iterar pelos elementos do primeiro conjunto e if para verificar a presença no segundo.

conjunto1 = {"a", "b"}
conjunto2 = {"a", "b", "c"}

subconjunto = True

for elemento in conjunto1:
  if elemento not in conjunto2:
    subconjunto = False
    break

if subconjunto:
  print(f"O conjunto {conjunto1} é subconjunto do conjunto {conjunto2}.")
else:
  print(f"O conjunto {conjunto1} não é subconjunto do conjunto {conjunto2}.")