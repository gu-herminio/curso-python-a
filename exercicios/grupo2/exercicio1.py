#Pergunte um número. Diga se este numero é par ou ímpar, escrevendo na tela.

def validacao(numero):
    if (numero % 2 == 0):
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")
        

numero = int(input("Digite um número para descobrir se é par ou ímpar:"))
validacao(numero)






        


