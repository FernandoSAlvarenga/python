import minha_calculadora.Calculadora 
from minha_calculadora.Calculadora import calcular as calc 



calculadora = minha_calculadora.Calculadora


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
calculadora.calcular(numero1, numero2)
calc(numero1, numero2)
minha_calculadora.Calculadora.calcular(numero1,numero2)