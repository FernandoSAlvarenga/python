class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __repr__(self):
        return f"Fracao({self.numerador}, {self.denominador})"

    def __add__(self, outra_fracao):
        novo_numerador = self.numerador * outra_fracao.denominador + self.denominador * outra_fracao.numerador
        novo_denominador = self.denominador * outra_fracao.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __sub__(self, outra_fracao):
        novo_numerador = self.numerador * outra_fracao.denominador - self.denominador * outra_fracao.numerador
        novo_denominador = self.denominador * outra_fracao.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __mul__(self, outra_fracao):
        novo_numerador = self.numerador * outra_fracao.numerador
        novo_denominador = self.denominador * outra_fracao.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __truediv__(self, outra_fracao):
        novo_numerador = self.numerador * outra_fracao.denominador
        novo_denominador = self.denominador * outra_fracao.numerador
        return Fracao(novo_numerador, novo_denominador)

    def __eq__(self, outra_fracao):
        return self.numerador * outra_fracao.denominador == self.denominador * outra_fracao.numerador

    def __gt__(self, outra_fracao):
        return self.numerador * outra_fracao.denominador > self.denominador * outra_fracao.numerador

    def __lt__(self, outra_fracao):
        return self.numerador * outra_fracao.denominador < self.denominador * outra_fracao.numerador

    def simplificar(self):
        m = max(self.numerador, self.denominador)
        for i in range(2, m + 1):
            if self.numerador % i == 0 and self.denominador % i == 0:
                self.numerador //= i
                self.denominador //= i
        return self

# Exemplo de uso
fracao1 = Fracao(10, 15)
fracao2 = Fracao(3, 2)

print(f"Fração 1: {fracao1}")  # Saída: 10/15
print(f"Fração 2: {fracao2}")  # Saída: 3/2

soma = fracao1 + fracao2
print(f"Soma: {soma}")  # Saída: 29/30

diferenca = fracao1 - fracao2
print(f"Diferença: {diferenca}")  # Saída: 1/30

multiplicacao = fracao1 * fracao2
print(f"Multiplicação: {multiplicacao}")  # Saída: 1/5

divisao = fracao1 / fracao2
print(f"Divisão: {divisao}")  # Saída: 2/5

comparacao_igualdade = fracao1 == fracao2
print(f"Fração 1 igual a Fração 2? {comparacao_igualdade}")  # Saída: False

comparacao_maior = fracao1 > fracao2
print(f"Fração 1 maior que Fração 2? {comparacao_maior}")  # Saída: False

comparacao_menor = fracao1 < fracao2
print(f"Fração 1 menor que Fração 2? {comparacao_menor}")  # Saída: True

fracao1_simplificada = fracao1.simplificar()
print(f"Fração 1 simplificada: {fracao1_simplificada}")  # Saída: 2/3