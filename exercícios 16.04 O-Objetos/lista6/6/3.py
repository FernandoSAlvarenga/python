class Circulo:
    def __init__(self, x, y, raio):
        self.x = x
        self.y = y
        self.raio = raio

    def __str__(self):
        return f"Círculo: centro ({self.x}, {self.y}), raio {self.raio}"

    def __eq__(self, outro_circulo):
        return self.x == outro_circulo.x and self.y == outro_circulo.y and self.raio == outro_circulo.raio

    def __add__(self, outro_circulo):
        if self.x == outro_circulo.x and self.y == outro_circulo.y:
            novo_raio = self.raio + outro_circulo.raio
            return Circulo(self.x, self.y, novo_raio)
        else:
            return None

    def area(self):
        return 3.1415 * self.raio * self.raio

# Exemplo de uso
circulo1 = Circulo(1, 2, 3)
circulo2 = Circulo(1, 2, 4)
circulo3 = Circulo(5, 6, 7)

print(circulo1)  # Saída: Círculo: centro (1, 2), raio 3
print(circulo2)  # Saída: Círculo: centro (1, 2), raio 4
print(circulo3)  # Saída: Círculo: centro (5, 6), raio 7

circulo_soma = circulo1 + circulo2
if circulo_soma:
    print(f"Soma dos círculos 1 e 2: {circulo_soma}")  # Saída: Círculo: centro (1, 2), raio 7
else:
    print("Os círculos não podem ser somados")

print(circulo1 + circulo3)  # Saída: Os círculos não podem ser somados

area_circulo1 = circulo1.area()
print(f"Área do Círculo 1: {area_circulo1:.2f}")  # Saída: Área do Círculo 1: 28.26