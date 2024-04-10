#Crie um dicionário que mapeie nomes de países para suas capitais. Utilize o método get() para buscar a capital de um país específico,
# tratando o caso de chave inexistente.

paises = {'Chile':'Santiago', 'Argentina': 'Buenos Aires', 'Uruguai': 'Montevidéu', 'Paraguai': 'Assunção', 'Brasil': 'Brasília', 'Bolívia': 'La Paz'}

pais = "panama"

capital = paises.get(pais)

if capital in None:
    print(f'')