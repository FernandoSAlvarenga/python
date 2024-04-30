
from abc import ABC, abstractmethod

class Jogo(ABC):
  def __init__(self, nome, genero, plataforma, classificacao_indicativa):
    self.nome = nome
    self.genero = genero
    self.plataforma = plataforma
    self.classificacao_indicativa = classificacao_indicativa

  @abstractmethod
  def iniciar(self):
    pass

  @abstractmethod
  def pausar(self):
    pass

  @abstractmethod
  def salvar_jogo(self):
    pass

  @abstractmethod
  def carregar_jogo(self):
    pass

class RPG(Jogo):
 
  def __init__(self, nome, genero, plataforma, classificacao_indicativa, sistema_batalha, mundo_aberto):
    super().__init__(nome, genero, plataforma, classificacao_indicativa)
    self.sistema_batalha = sistema_batalha
    self.mundo_aberto = mundo_aberto

  def iniciar(self):
    print(f"Iniciando jogo RPG: {self.nome}")
    print(f"Sistema de batalha: {self.sistema_batalha}")
    if self.mundo_aberto:
      print("Mundo aberto disponível para exploração!")
    else:
      print("História linear com eventos pré-definidos.")

  def pausar(self):
    print(f"Jogo RPG {self.nome} pausado.")

  def salvar_jogo(self):
    print(f"Progresso do jogo RPG {self.nome} salvo.")

  def carregar_jogo(self):
    print(f"Carregando jogo RPG {self.nome}.")

class Aventura(Jogo):
  """Subclasse para representar um jogo de aventura."""

  def __init__(self, nome, genero, plataforma, classificacao_indicativa, narrativa, foco_exploracao):
    super().__init__(nome, genero, plataforma, classificacao_indicativa)
    self.narrativa = narrativa
    self.foco_exploracao = foco_exploracao

  def iniciar(self):
    print(f"Iniciando jogo de aventura: {self.nome}")
    print(f"Narrativa: {self.narrativa}")
    if self.foco_exploracao:
      print("Foco principal na exploração e resolução de enigmas.")
    else:
      print("História linear com foco na narrativa.")

  def pausar(self):
    print(f"Jogo de aventura {self.nome} pausado.")

  def salvar_jogo(self):
    print(f"Progresso do jogo de aventura {self.nome} salvo.")

  def carregar_jogo(self):
    print(f"Carregando jogo de aventura {self.nome}.")

class Estrategia(Jogo):
 

  def __init__(self, nome, genero, plataforma, classificacao_indicativa, recursos_gerenciamento, foco_competitivo):
    super().__init__(nome, genero, plataforma, classificacao_indicativa)
    self.recursos_gerenciamento = recursos_gerenciamento
    self.foco_competitivo = foco_competitivo

  def iniciar(self):
    print(f"Iniciando jogo de estratégia: {self.nome}")
    print(f"Gerenciamento de recursos: {self.recursos_gerenciamento}")
    if self.foco_competitivo:
      print("Foco principal na competição com outros jogadores.")
    else:
      print("Campanha single-player ou modo cooperativo.")

  def pausar(self):
    print(f"Jogo de estratégia {self.nome} pausado.")

  def salvar_jogo(self):
    print(f"Progresso do jogo de estratégia {self.nome} salvo.")

  def carregar_jogo(self):
    print(f"Carregando jogo de estratégia {self.nome}.")


jogo_rpg = RPG("The Witcher 3", "RPG de Ação", "PC, PS4, Xbox One", "M", "Turnos", True)
jogo_aventura = Aventura("Uncharted 4", "Aventura", "PS4", "12+", "Cinemática", True)
jogo_estrategia = Estrategia("StarCraft II", "Estratégia em Tempo Real", "PC", "12+","Cinemática", True)


jogo_rpg.iniciar()
jogo_rpg.carregar_jogo()
jogo_rpg.pausar()   
jogo_rpg.salvar_jogo()


jogo_aventura.iniciar()
jogo_aventura.carregar_jogo()
jogo_aventura.pausar()   
jogo_aventura.salvar_jogo()


jogo_estrategia.iniciar()
jogo_estrategia.carregar_jogo()
jogo_estrategia.pausar()   
jogo_estrategia.salvar_jogo()

