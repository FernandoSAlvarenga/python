
livros_lidos = {"Dom quixote", "Orgulho e preconceito", "O grande gatsby", "100 anos de solidão", "1984"}
livros_desejados = {"1984", "O Senhor dos Anéis", "Crime e Castigo", "O Pequeno Príncipe"}

livros_nao_lidos = set()

for livro in livros_desejados:
    if livro not in livros_lidos:
        livros_nao_lidos.add(livro)
        print(livros_nao_lidos)

print("Livros que você ainda não leu:")
for livro in livros_nao_lidos:
    print(livro)