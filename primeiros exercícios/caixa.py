import random
import string
from tqdm import tqdm
import time



class banco :
def __init__ (self, titular, codigo) : 
    self.titular: titular
    self.numero_conta = ''.join(random.choices(string.digits, k=5))
    self.saldo = 0
    self.codigo = codigo
    self.usuario = usuario

#Realizar depósito#
def depositar(self, valor):
    self.saldo += valor
    print()
    print('Atualizando depósito...')
    for i in tqdm(range(2)):
        time.sleep
    print()
    print(f'Depósito realizado com sucesso! Novo saldo: R${self.saldo:.2f}')

#Realizar saque#
def sacar(self, valor):
    if valor > self.saldo:
    print()
    print('Atualizando saque...')
    for i in tqdm(range(2)):
        time.sleep(1)
    print()
    print('Saldo insuficiente.')
    else:
    self.saldo -= valor
    print()
    print('Atualizando saque...')
    for i in tqdm(range(2)):
        time.sleep(1)
    print()
    print(f'Saque realizado com sucesso! Novo saldo: R${self.saldo:.2f}')

#Realizar consulta de saldo#    
def consultar(self):
    print()
    print('Atualizando saldo...')
    for i in tqdm(range(2)):
        time.sleep(1)
    print()
    print(f'Titular: {self.titular}')
    print(f'Número da conta: {self.numero_conta}')
    print(f'Saldo: R${self.saldo:.2f}')

#Realizar tranferencia# 
def transferir(self, valor, numero_conta):
    if valor > self.saldo:
    print()
    print('Atualizando tranferência...')
    for i in tqdm(range(2)):
        time.sleep(1)
    print()
    else:
    self.saldo -= valor
    numero_conta.saldo += valor
    print()
    print('Atualizando transferência...')
    for i in tqdm(range(2)):
        time.sleep(1)
    print()
    print(f'Transferência realizada com sucesso para a conta {conta.numero_conta}!')    

#Criar conta#       
    while True:
        usuario = input('Cadastre seu nome: ')
    if all(c.isalpha() for c in usuario):
    break
    else:
    print('Somente letras!')

    while True:
        senha = input('Cadastre sua senha: ')
    if all (c.isnumeric() for c in senha):
    break
    else:
    print('Somente números!')
    print()
    print('Criando conta...')
    for i in tqdm(range(2)):
        time.sleep(1)
        
    nome = input('Digite seu nome: ')
    while nome != usuario:
    nome = input('Nome incorreto! Digite novamente: ')
    validar = input('Digite sua senha: ')
    while validar != senha:
    validar = input('Senha incorreta! Digite novamente: ')
    else:
    print(f'Bem vindo(a) {usuario}')

    conta = banco(usuario, senha)
    conta.numero_conta = random.randint(10000, 99999)
    print()
    print(f'Sua conta foi criada com sucesso! Seu número de conta é: {conta.numero_conta}.')
    print()

    contas = []
            
    conta1 = banco(nome, validar)
    contas.append(conta1)

def login():
    while True:
        print('\n ------------  INÍCIO  -------------')
        print('1 - Cadastrar conta')
        print('2 - Entrar na conta')
        print('3 - Sair')
        menu = input('Digite a opção desejada:  ')

        if menu == '1':
            while True:
                cliente = input('Cadastre seu nome: ')
                if all(c.isalpha() for c in cliente):
                    break
                else:
                    print('Somente letras!')

            while True:
                codigo = input('Cadastre sua senha: ')
                if all(c.isnumeric() for c in codigo):
                    break
                else:
                    print('Somente números!')
                print()
                print(' Criando conta...')
                for i in tqdm(range(2)):
                    time.sleep(1)

                nome = input('Digite seu nome: ')
                while nome != cliente:
                    nome = input ('Nome incorreto! Digite novamente: ')
                validar = input('Digite sua senha: ')
                while validar != codigo:
                    validar = input('Senha incorreta! Digite novamente: ')
                else:
                    print(f'Bem vindo(a) {cliente}')
                conta = banco(cliente, codigo)
                conta.numero_conta = random.randint(10000, 99999)
                print()
                print('  Carregando Sistema...')
                for i in tqdm(range(2)):
                    time.sleep(1)
                print()
                print(f'Sua conta foi criada com sucesso! O número da sua conta é: {conta.numero_conta}.')
                print()
                while True:
                    print('\n ------------  MENU  ------------')
                    print('1 - Consultar Saldo')
                    print('2 - Depositar')
                    print('3 - Sacar')
                    print('4 - Transferir')
                    print('5 - Sair')
                    opcao = input('Digite a opção desejada: ')

                    if opcao == '1':
                        conta.consultar()
                    elif opcao == '2':
                        valor = float(input('Digite valor a ser depositado: R$'))
                        conta.depositar(valor)
                    elif opcao == '3':
                        valor = float(input('Digite o valor a ser sacado: R$'))
                        conta.sacar(valor)
                    elif opcao == '4':
                        valor = (float('Digite o valor a ser transferido: R$'))
                        outra_conta = (input('Digite o nome do titular que receberá a tranferencia: '))
                        if outra_conta.lower() == conta.titular.lower():
                            print('Não é possível transferir para a própria conta.')
                        else:
                            encontrou_conta = False
                            for c in contas:
                                if c.titular.lower() == outra_conta.lower():
                                    outra_conta = c
                                    encontrou_conta = True
                                    break
                            if encontrou_conta:
                                conta.transferir(valor, outra_conta)
                            else:
                                print('Titular da conta não encontrado.')
                    elif opcao == '5':
                     print()
                     print('Você saiu do programa...  \n')
                     login()
                else:
                    print('Opção inválida!')
        elif menu == '2':
            nome = input('Digite seu nome: ')
            while nome != usuario:
                nome = input('Nome incorreto! Digite novamente: ')
            validar = input('Digite sua senha: ')
            while validar != senha:
                validar = input('Senha incorreta! Digite novamente: ')
            else:
                print(f'Bem vindo de volta {usuario}')
                return menu
        elif menu == '3':
            print()
            quit('Você saiu do programa...  \n')
        else:
            print('Opção inválida!')

    while True:
        print('\n ------------  MENU  ------------')
        print('1 - Consultar Saldo')
        print('2 - Depositar')
        print('3 - Sacar')
        print('4 - Transferir')
        print('5 - Sair ')
        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            conta.consultar()
        elif opcao == '2':
            valor = float(input('Digite o valor a ser depositado: '))
            conta.depositar(valor)
        elif opcao == '3':
            valor = float(input('Digite o valor a ser sacado: R$'))
        elif opcao == '4':
            valor = float(input('Digite o valor a ser transferido: R$'))
            nome = input('Digite o nome do titular da conta que receberá a tranferência: ')
            if nome.lower() == nome.lower():
                print('Não é possível tranferir para a própria conta.')
            else:
                encontrou_conta = False
                for c in contas:
                    if c.titular.lower() == nome.lower():
                        nome = c
                        encontrou_conta = True
                        break
                if encontrou_conta:
                    conta.transferir(valor, nome)
                else:
                    print('Titular da conta não encontrado.')
        elif opcao == '5':
            print()
            print('Você saiu do programa...  \n')
            login()
        else:
            print('Opção inválida!')


if __name__ == '__main__':
    login()

                    
                

               
            
    

    