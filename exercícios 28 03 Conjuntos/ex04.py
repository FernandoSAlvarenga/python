# Escreva um programa que encontre a união de dois conjuntos. Utilize for para iterar pelos elementos de ambos os conjuntos e adicionar à lista final.

conjunto1 = {'a', 'b', 'c', 'd'}
conjunto2 = {'d', 'e', 'f', 'g'}

conjunto_soma = set()

for elemento in conjunto1:
    conjunto_soma.add(elemento)
    
for corredor in conjunto2:
    conjunto_soma.add(corredor)
    
print(f'Lista final: {conjunto_soma}')