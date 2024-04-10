# Crie dois dicionários com as informações de dois alunos e compare seus  nomes e idades. ok
#• Crie dois dicionários com as informações de dois produtos e compare seus preços. ok
#• Crie dois dicionários com as informações de dois livros e compare seus  autores. 
#• Crie dois dicionários com as informações de dois filmes e compare seus diretores.

aluno1 = {'nome':'Tay', 'idade': 14, 'nascimento':81}
aluno2 = {'nome':'Fernando', 'idade': 14, 'nascimento':81}


if aluno1['nome'] == aluno2['nome'] and aluno1['idade'] == aluno2['idade']:
    print(f'Os alunos tem a mesma idade e nome.')
else:
    print(f'Idade ou nome diferentes')
    
produto1 = {"nome": "Camiseta", "preço": 50.00, "cor": "Azul", "tamanho": "M"}
produto2 = {"nome": "Calça", "preço": 75.00, "cor": "Preta", "tamanho": "38"}

if produto1["preço"] == produto2["preço"]:
    print("Os produtos possuem o mesmo preço.")
else:
    print("Os produtos possuem preços diferentes.")
    
livro1 = { "titulo": "As duas Torres", "autor": "J. R. R. Tolkien", "ano_publicacao": 1954, "genero": "Fantasia"}
livro2 = {"titulo": "O Senhor dos Anéis", "autor": "J. R. R. Tolkien", "ano_publicacao": 1954, "genero": "Fantasia" }

if livro1["autor"] == livro2["autor"]:
    print("Os livros possuem o mesmo autor.")
else:
    print("Os livros possuem autores diferentes.")
    
filme1 = { "nome": "O Senhor dos Anéis", "diretor": "Peter Jackson", "ano_lancamento": 2001, "genero": "Fantasia" }
filme2 = { "nome": "Hobbit", "diretor": "Peter Jackson", "ano_lancamento": 2014, "genero": "Fantasia"}

if filme1["diretor"] == filme2["diretor"]:
    print("Os filmes possuem o mesmo diretor.")
else:
    print("Os filmes possuem diretores diferentes.")