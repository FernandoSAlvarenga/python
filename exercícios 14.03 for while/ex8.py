secret = 'CAPACETE'
letra_dig = []
tentativas = 0

print('JOGO DA FORCA EM PYTHON')

while True:
    print(tentativas)
    letra = str(input('Digite uma letra: ')).upper() #.upper() usado para converter caixa baixa para caixa alta
    if len(letra)> 1:
        print('Digite UMA letra, signifa: Digite UMA letra.')
        continue
    letra_dig.append(letra)
    
    secret_temp = ''
    for letra_secret in secret:
        if letra_secret in letra_dig:
            secret_temp += letra_secret
        else:
            secret_temp += '*'
    if secret_temp == secret:
        print('Você venceu, uhuu, salvou o universo!')
        break
    else:
        print(f'A palavra Secreta esta assim: {secret_temp}')
        
    if letra not in secret:
        tentativas += 1 # aqui estava a opção -=1, ele descontava as tentativas que iniciavam de 0. 
        
    if tentativas >= 3: # esse é meu limitador, como ele descontava, ficava negativo " -1, -2, -3 etc.. nunca iria chegar neste limitador 3 positivo. "
        print('Você Perdeu! Não deprima, só um jogo!')
        break
    
    