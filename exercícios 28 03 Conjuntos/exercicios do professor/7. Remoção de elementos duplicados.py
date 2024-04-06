#7. Remoção de elementos duplicados:
#Escreva um programa que remova elementos duplicados de uma lista e crie um conjunto. Utilize while para iterar pelo conjunto e if para verificar a presença de elementos duplicados.

conjunto_lista = ["a", "a", "b", "c", "c"]

conjunto_sem_duplicados = set()

for elemento in conjunto_lista:
  if elemento not in conjunto_sem_duplicados:
    conjunto_sem_duplicados.add(elemento)

print(f"Conjunto sem duplicados: {conjunto_sem_duplicados}")

