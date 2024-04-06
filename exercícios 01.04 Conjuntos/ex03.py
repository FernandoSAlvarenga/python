# 3. Diferença de Conjuntos: Crie um conjunto com os livros que você já leu e outro com os livros que você deseja ler.
# Encontre os livros que você ainda não leu e imprima a lista.

livros_lidos={'sol', 'lua', 'ceu'}
livros_desejados={'terra', 'mar', 'ceu'}

livros_naolidos = livros_desejados.difference(livros_lidos)
print(f'Os livros que ainda não li foram:{livros_naolidos}')