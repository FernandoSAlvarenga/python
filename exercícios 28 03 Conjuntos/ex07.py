# Escreva um programa que remova elementos duplicados de um conjunto. Utilize while para iterar
# pelo conjunto e if para verificar a presença de elementos duplicados

conjunto_1 = set()
conjunto_sem_duplicado = set()

conjunto_nulo = set()


while True:
    print('BEM VINDO!' *16)
    tecla_parada = input("Cadastre uma tecla de parada (Ex.: /*-+. ): ")
    if not tecla_parada.isdigit():#A função isdigit() verifica se a string digitada é composta apenas por dígitos. Se a string digitada for um número inteiro, uma mensagem de erro é exibida e o usuário é solicitado a digitar novamente.
        break
    else:
        print("Somente caracteres (ex. /*-+).")
        
while True:
    valor = input('Digite números do conjunto: ')
    if valor == tecla_parada and conjunto_nulo != ():
                
        break
    elif not valor.isdigit():
        print(f"Somente números ou a tecla de parada: {tecla_parada} .")

    else:
        valor = int(valor)
        conjunto_1.add(valor)

for elemento in conjunto_1:
    if elemento not in conjunto_sem_duplicado:
        conjunto_sem_duplicado.add(elemento)
print(f'Conjunto sem duplicados: {conjunto_sem_duplicado}')        
