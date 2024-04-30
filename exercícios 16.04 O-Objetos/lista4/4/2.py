class ProdutoEletronico:
 

  def __init__(self, codigo, nome, marca, modelo, preco, tipo):
    self._codigo = codigo
    self._nome = nome
    self._marca = marca
    self._modelo = modelo
    self._preco = preco
    self._tipo = tipo
    self._garantia_estendida = False
    self._preco_garantia = 0

  def aplicar_garantia_estendida(self):
    if not self._garantia_estendida:
      # Adiciona garantia estendida e atualiza preço
      self._garantia_estendida = True
      if self._tipo == "Celular":
        self._preco_garantia = 50
      elif self._tipo == "Notebook":
        self._preco_garantia = 100
      else:
        self._preco_garantia = 20
      self._preco += self._preco_garantia

  def calcular_valor_total(self):
    return self._preco

  def mostrar_informacoes(self):
    garantia_str = "Com" if self._garantia_estendida else "Sem"
    print(f"""
    Produto Eletrônico: {self._codigo}
    Nome: {self._nome}
    Marca: {self._marca}
    Modelo: {self._modelo}
    Preço: R${self._preco:.2f}
    Tipo: {self._tipo}
    Garantia Estendida: {garantia_str} ({self._preco_garantia:.2f})
    """)

# Exemplo de uso
produto1 = ProdutoEletronico("PE1234", "Smartphone", "Samsung", "Galaxy S23", 3500.00, "Celular")

produto1.mostrar_informacoes()

produto1.aplicar_garantia_estendida()

produto1.mostrar_informacoes()

produto1.calcular_valor_total()  # Valor total já inclui garantia
print(f"Valor total com garantia: R${produto1.calcular_valor_total():.2f}")