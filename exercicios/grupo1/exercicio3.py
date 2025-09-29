#início
print("======================= Cálculo de média escolar =======================")
nome_aluno = input("Preencha o nome do aluno: ")
n1 = int(input(f"Digite a nota 1 do aluno {nome_aluno}: "))
n2 = int(input(f"Digite a nota 2 do aluno {nome_aluno}: "))
n3 = int(input(f"Digite a nota 3 do aluno {nome_aluno}: "))
n4 = int(input(f"Digite a nota 4 do aluno {nome_aluno}: "))


# Cálculo da média 
media = (n1+n2+n3+n4) / 4

#Validação de média
if media < 5:
    situacao = "Reprovado."
elif media >= 5 and media < 7:
    situacao = "Recuperação."
else:
    situacao = "Aprovado."

#Retorno final
print(f"A média do aluno {nome_aluno} foi {media} e a sua situação é: {situacao}")




