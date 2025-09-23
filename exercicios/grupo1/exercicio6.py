#Calcule a área de um círculo com base no raio informado. Como calcular: A = PI . R ao quadrado

#Import do método pi para cálculo da área
from math import pi


#Início
print(f"=============================Calculadora de área=============================")
raio = float(input("Digite o valor em centimetros do raio do círculo que deseja calcular: "))

#Cálculo
area = pi * (raio ** 2)

#Resultado final
print(f"O resultado do cálculo da área é: {area:.2f}cm². ")