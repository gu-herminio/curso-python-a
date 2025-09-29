#Pergunte a data de nascimento e verifique se a data atual é a data de aniversário. Se for, printe a mensagem de Feliz Aniversário, senão printe a mensagem hoje e dia X de Y de ZZZZ.


#importe das biblioteca importantes para recebimento e validação de datas
from datetime import date,datetime


#funcao para comparar as data de nascimento equivale a data de hoje
def valida_data_nascimento(data_nascimento,data_hoje):
    if  (data_nascimento.day == data_hoje.day and data_nascimento.month == data_hoje.month):
        print(f"Hoje é seu aniversário ({data_hoje.strftime('%d/%m/%Y')}), Feliz aniversário!!!!!")
    else:
        print(f"Hoje é dia {data_hoje.strftime('%d de %B de %Y')}")


#Recebendo dados, usando Try-Except para informar o erro quando o usuário inserir no formato incorreto
try:    
    data_hoje = date.today()
    data_nascimento = input("Por favor, digite sua data de nascimento (DD/MM/AAAA): ")


    #Conversão da data de nascimento para date
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()


    #Inicia função para validação e retorno do resultado
    valida_data_nascimento(data_nascimento,data_hoje)


except ValueError:
    print("Erro: Formato de data inválido. Certifique-se de usar DD/MM/AAAA.")



