#Pergunte um número. Diga se este numero faz parte da tabuada do 3, escrevendo na tela.

#Biblioteca sympy, para utilizar a função mod que retorna o resto da divisão de outra maneira
from sympy import Mod

def valida_numero(numero):
    if (numero % 3 == 0):
        print(f"O número {numero} pertence a tabuada de 3.")
    else:
        print(f"O número {numero} não pertence a tabuada de 3.")


# A mesma função anterior porém usando biblioteca Sympy para treinar a utilidade da VENV assim como citei no exercicio 2
def valida_numero_biblioteca(numero,divisor = 3):
    resto = Mod(numero,divisor)

    if (resto == 0):
        print(f"O número {numero} pertence a tabuada de 3.")
    else:
        print(f"O número {numero} não pertence a tabuada de 3.")


#Retorno final
numero = int(input("Digite um número para descobrir se pertence a tabuada de 3: "))
valida_numero(numero)
valida_numero_biblioteca(numero)