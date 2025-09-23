#Calcule a área de um retângulo. Area = comprimento * altura

#Inicio
print(f"=============================Calculadora de área=============================")
comprimento = float(input("Digite o valor em centimetros do comprimento do retângulo: "))
altura = float(input("Digite o valor em centímetros da altura do retângulo: "))

#Cálculo
area = comprimento * altura

print(f"Á área do retângulo cujo altura possui {altura:.2f} cm e comprimento de {comprimento:.2f} cm é: {area:.2f} cm².")
