#3. Diferença de conjuntos: 
#Escreva um programa que encontre a diferença entre dois conjuntos. Utilize for para iterar pelos 
#elementos e if para verificar a presença no primeiro conjunto e não no segundo.

conjunto1 = {1, 2, 3, 4, 5, 6}
conjunto2 = {4, 5, 6, 7, 8, 9}

diferenca = set()



for elemento in conjunto1:
  # Verifique se o elemento está em apenas um dos conjuntos
  if elemento not in conjunto2 or elemento in conjunto1 and elemento not in conjunto2:
    diferenca.add(elemento)

for elemento in conjunto2:
  # Verifique se o elemento está em apenas um dos conjuntos (considerando conjunto2)
  if elemento not in conjunto1 or elemento in conjunto2 and elemento not in conjunto1:
    diferenca.add(elemento)

print("Diferença simétrica:", diferenca)