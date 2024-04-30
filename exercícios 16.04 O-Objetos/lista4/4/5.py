class JogoEletronico:
  

  def __init__(self, nome, genero, plataforma, classificacao_indicativa, preco):
    self._nome = nome
    self._genero = genero
    self._plataforma = plataforma
    self._classificacao_indicativa = classificacao_indicativa
    self._preco = preco
    self._desconto = 0

  def aplicar_desconto(self, desconto):
    if 0 <= desconto <= 1:
      self._desconto = desconto
    else:
      print("Valor de desconto inválido. Deve ser entre 0 e 1.")

  def calcular_valor_total(self):
    preco_final = self._preco * (1 - self._desconto)
    return preco_final

  def mostrar_informacoes(self):
    desconto_str = f"{self._desconto * 100:.0f}%" if self._desconto else "0%"
    preco_final = self.calcular_valor_total()
    print(f"""
    Jogo Eletrônico: {self._nome}
    Gênero: {self._genero}
    Plataforma: {self._plataforma}
    Classificação Indicativa: {self._classificacao_indicativa}
    Preço Base: R${self._preco:.2f}
    Desconto: {desconto_str}
    Preço Final: R${preco_final:.2f}
    """)

# Exemplo de uso
jogo1 = JogoEletronico("The Witcher 3", "RPG", "PC e Consoles", "16 anos", 199.90)

jogo1.mostrar_informacoes()

jogo1.aplicar_desconto(0.2) 
jogo1.mostrar_informacoes()

jogo1.aplicar_desconto(1.5)  
jogo1.mostrar_informacoes()