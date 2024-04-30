from datetime import datetime, timedelta

class Voo:
 

  def __init__(self, codigo, companhia, origem, destino, horario_saida, horario_chegada, preco_passagem):
    self._codigo = codigo
    self._companhia = companhia
    self._origem = origem
    self._destino = destino
    self._horario_saida = horario_saida
    self._horario_chegada = horario_chegada
    self._preco_passagem = preco_passagem

  def calcular_duracao_voo(self):
    duracao_minutos = (self._horario_chegada - self._horario_saida).total_seconds() / 60
    duracao_horas = duracao_minutos / 60
    return duracao_horas

  def aplicar_desconto(self, desconto):
    if 0 <= desconto <= 1:
      novo_preco = self._preco_passagem * (1 - desconto)
      self._preco_passagem = novo_preco
    else:
      print("Valor de desconto inválido. Deve ser entre 0 e 1.")

  def mostrar_informacoes(self):
    print(f"""
    Voo: {self._codigo}
    Companhia: {self._companhia}
    Origem: {self._origem}
    Destino: {self._destino}
    Horário de Saída: {self._horario_saida.strftime('%d/%m/%Y %H:%M')}
    Horário de Chegada: {self._horario_chegada.strftime('%d/%m/%Y %H:%M')}
    Duração: {self.calcular_duracao_voo():.2f} horas
    Preço da Passagem: R${self._preco_passagem:.2f}
    """)


voo1 = Voo("JJ1234", "LATAM", "Guarulhos (GRU)", "Galeão (GIG)", datetime(2024, 4, 23, 20, 0), datetime(2024, 4, 23, 21, 30), 250.00)

voo1.mostrar_informacoes()

voo1.aplicar_desconto(0.2)  # Aplica 20% de desconto
voo1.mostrar_informacoes()