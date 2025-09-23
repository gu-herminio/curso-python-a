"""(DESAFIO DA SEMANA): Você está montando um cadastro para uma empresa de vendas na internet, e precisa fornecer este "formulário de dados de clientes". Não se preocupe neste momento se irá ou não guardar este dado em algum lugar. Pergunte e obtenha os seguintes dados e depois exiba todos na tela:
Nome Completo
Data de Nascimento
Cidade/País de Origem(Nascimento)
Endereço completo de onde mora
País onde reside
Data do Cadastro
Escolaridade: (Ensino Básico/Ensino Fundamental/Ensino Superior)"""


#import biblioteca datetime para pegar a data do sistema
from datetime import date

#Início

# Cadastro de Cliente

# Introdução
print("-------------Bem vindo ao formulário de cadastro de clientes-------------")

# Preenchimento de dados
nome = input("Inicie o cadastro preenchendo o seu nome completo: ")
data_nascimento = input("Preencha a sua data de nascimento (dd/mm/aaaa): ")
cidade_pais_origem = input("Preencha a cidade e o país de origem: ")
endereco = input("Preencha o endereço completo: ")
pais_reside = input("Preencha o país onde atualmente reside: ")
data_cadastro = date.today()
escolaridade = input("Informe o seu grau de escolaridade: ")

# Retorno final
print("\n-------------Segue abaixo as informações preenchidas:-------------")
print(f"Nome completo: {nome}")
print(f"Data de Nascimento: {data_nascimento}")
print(f"Cidade e País de Origem: {cidade_pais_origem}")
print(f"Endereço: {endereco}")
print(f"País onde atualmente reside: {pais_reside}")
print(f"Data do cadastro: {data_cadastro.strftime('%d/%m/%Y')}")
print(f"Grau de escolaridade: {escolaridade}")