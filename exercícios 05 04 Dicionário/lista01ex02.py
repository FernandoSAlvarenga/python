#Crie um dicionário com as informações de um amigo e acesse o valor da  chave "nome". 
#Crie um dicionário com as informações de um produto e acesse o valor da chave "preço".

dicionario_amigo = {'nome':'Tay', 'idade': 14}
dicionario_produto = {'nome':'capacete','preco':600, 'cor':'branco','tamanho':60}

nome_amigo = dicionario_amigo.get('nome', 'Não informado')
preco_produto = dicionario_produto.get('preco', 'Não informado')

print(f'Nome do amigo: {nome_amigo}')
print(f'Preço do produto é: {preco_produto}')
