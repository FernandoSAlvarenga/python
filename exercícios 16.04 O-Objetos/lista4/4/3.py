class Restaurante:
  

  def __init__(self, nome, especialidade, endereco, horario_funcionamento):
    self._nome = nome
    self._especialidade = especialidade
    self._endereco = endereco
    self._horario_funcionamento = horario_funcionamento
    self._cardapio = {}

  def adicionar_prato(self, nome_prato, descricao, preco):
    if nome_prato not in self._cardapio:
      self._cardapio[nome_prato] = {"descricao": descricao, "preco": preco}
      print(f"Prato '{nome_prato}' adicionado com sucesso ao cardápio!")
    else:
      print(f"Prato '{nome_prato}' já existe no cardápio. Operação ignorada.")

  def remover_prato(self, nome_prato):
    if nome_prato in self._cardapio:
      del self._cardapio[nome_prato]
      print(f"Prato '{nome_prato}' removido do cardápio com sucesso!")
    else:
      print(f"Prato '{nome_prato}' não encontrado no cardápio. Operação ignorada.")

  def mostrar_cardapio(self):
    if self._cardapio:
      print(f"\n**Cardápio - {self._nome}**")
      for nome_prato, dados_prato in self._cardapio.items():
        descricao = dados_prato["descricao"]
        preco = dados_prato["preco"]
        print(f"{nome_prato}: {descricao} - R${preco:.2f}")
    else:
      print(f"O cardápio do restaurante {self._nome} está vazio no momento.")

# Exemplo de uso
restaurante1 = Restaurante("Cantinho Mineiro", "Comida caseira", "Rua Silva Xavier, 123", "12h às 23h")

restaurante1.mostrar_cardapio()  

restaurante1.adicionar_prato("Feijoada", "Feijoada completa com arroz, couve, laranja e torresmo", 25.90)
restaurante1.adicionar_prato("Strogonoff", "Strogonoff de carne com purê de batata", 19.90)
restaurante1.adicionar_prato("Feijoada", "Sopa de feijão com legumes", 12.00)  # Erro: prato já existe

restaurante1.mostrar_cardapio()

restaurante1.remover_prato("Strogonoff")
restaurante1.remover_prato("Feijoada Inexistente") 

restaurante1.mostrar_cardapio()