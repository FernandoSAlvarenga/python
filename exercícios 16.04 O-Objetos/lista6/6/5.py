class Data:
    def __init__(self, dia, mes, ano):
        if not self.valida_data(dia, mes, ano):
            raise ValueError("Data inválida")
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def valida_data(self, dia, mes, ano):
        if not (1 <= dia <= 31) or not (1 <= mes <= 12) or ano < 1:
            return False
        dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if mes == 2 and ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            dias_no_mes[1] = 29
        return dia <= dias_no_mes[mes - 1]

    def __str__(self):
        return f"{self.dia:02}/{self.mes:02}/{self.ano}"

    def __eq__(self, outra_data):
        return self.dia == outra_data.dia and self.mes == outra_data.mes and self.ano == outra_data.ano

    def __lt__(self, outra_data):
        if self.ano < outra_data.ano:
            return True
        elif self.ano == outra_data.ano and self.mes < outra_data.mes:
            return True
        elif self.ano == outra_data.ano and self.mes == outra_data.mes and self.dia < outra_data.dia:
            return True
        else:
            return False

    def __gt__(self, outra_data):
        return not self.__lt__(outra_data)

    def __add__(self, dias):
        if not isinstance(dias, int) or dias < 0:
            raise TypeError("Dias deve ser um inteiro positivo")
        nova_data = Data(self.dia, self.mes, self.ano)
        nova_data.dia += dias
        while nova_data.dia > self.dias_no_mes(nova_data.mes, nova_data.ano):
            nova_data.dia -= self.dias_no_mes(nova_data.mes, nova_data.ano)
            nova_data.mes += 1
            if nova_data.mes > 12:
                nova_data.mes = 1
                nova_data.ano += 1
        return nova_data

    def dias_no_mes(self, mes, ano):
        dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if mes == 2 and ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            dias_no_mes[1] = 29
        return dias_no_mes[mes - 1]

# Exemplo de uso
data1 = Data(10, 5, 2024)
data2 = Data(15, 6, 2023)
data3 = Data(31, 12, 2022)  # Erro: Data inválida

print(f"Data 1: {data1}")  # Saída: 10/05/2024
print(f"Data 2: {data2}")  # Saída: 15/06/2023

data_futura = data1 + 30
print(f"Data 1 mais 30 dias: {data_futura}")  # Saída: 10/06/2024

data_maior = data1 > data2
print(f"Data 1 maior que Data 2? {data_maior}")  # Saída: True

data_igual = data1 == data2
print(f"Data 1 igual à Data 2? {data_igual}")  # Saída: False