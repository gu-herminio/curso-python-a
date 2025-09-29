#Pergunte um número. Diga se este numero é primo ou não, escrevendo na tela.

## P.S Estou usando o método da função sympy para testar a criação de uma VENV, as bibliotecas necessárias estão presente no arquivo requirements.txt

## instalar bibiliotecas no arquivo requirements:  "pip install -r requirements.txt no terminal"

from sympy import isprime

def valida_primo(numero):
    if isprime(numero) == True:
        return f"{numero} é primo."
    else:
        return f"{numero} não é primo."

#Retorno final
numero = int(input("Digite um número para saber se é primo ou não: "))
print(valida_primo(numero))