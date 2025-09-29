#Pergunte dados de um produto (Nome, Fabricante, Preço). Caso o mesmo inicie com uma vogal, acrescente *** (3 asteriscos) ao nome do produto. Ao final exiba todos os dados do produto.


#Recebimento de dados
print("----------------------------- CADASTRO DE PRODUTOS ----------------------------- ")
nome_produto = input("Digite o nome do produto: ")
fabricante_produto = input("Digite o nome da fabricante: ")
preco_produto = float(input("Digite o preço do produto: "))


#Análise inicial do produto
inicial_produto = nome_produto[0].lower()

if inicial_produto in "aeiouáéíóúàèìòùâêîôûãõ":
    nome_produto = nome_produto + "***"


#exibição de dados final
print(f"O produto {nome_produto} da fabricante {fabricante_produto} foi cadastrado com o preço de R${preco_produto}.")