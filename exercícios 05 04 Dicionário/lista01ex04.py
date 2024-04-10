#Crie um dicionário com as informações de um amigo e imprima cada chave e valor em linhas separadas. 
#• Crie um dicionário com as informações de um produto e imprima todos os valores em uma única linha. 
#• Crie um dicionário com as informações de um livro e imprima as chaves "título" e "autor" em uma única linha. 
#• Crie um dicionário com as informações de um filme e imprima as chaves "nome" e "diretor" em uma única linha. 

dicionario_amigo = {'nome':'Tay', 'idade': 14, 'nascimento':81}

print(f"Dados do amigo: {dicionario_amigo.get("nome")}")
print(f"Dados do amigo: {dicionario_amigo.get("idade")}")
print(f"Dados do amigo: {dicionario_amigo.get("nascimento")}")

dicionario_produto = {'nome':'capacete','preco':600,'cor':'branco','tamanho':60}
for chave, valor in dicionario_produto.items():
    print(f"Chave: {chave}, Valor: {valor}")

dicionario_livro = {'nome':'maktub','preco':'37,29','cor':'vermelho','tamanho':'197'}
print(f"Dados do Livro: {dicionario_livro.get('nome'), dicionario_livro.get('cor')}")


dicionario_filme = {'filme':'Não Olhe Para Cima','diretor':'Adam McKay','lancamento': 2021,'genero':'Drama'}
print(f"Dados do Livro: {dicionario_filme.get('filme'), dicionario_filme.get('diretor')}")



#print(f'Dados do livros{dicionario_livro}')
#print(f'Dados do filme{dicionario_filme}')

