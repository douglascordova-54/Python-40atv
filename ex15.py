#Exemplo15- Desconto na compra
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler o valor de uma compra e mostrar o final a pagar.
#Compras apartir de R$ 100,00 ganham desconto de 10%.

#Entrada: Solicita o valor da compra
valor_Compra = float(input("Digite o valor da compra: "))

#Processamento: Calcula o valor do desconto
desconto = valor_Compra * 0.10

#Processamento: Calcula o valor total com desconto
valor_Total_Desc = valor_Compra - desconto

#Decisão 1: Verifica se o valor da compra e de 100 ou mais para aplicar o desconto
if valor_Compra >= 100:
    #Saída 1: Exibe valor total com desconto
    print("Valor final: R$ ", valor_Total_Desc)
#Caso restante
else:
    #Saída 2: Exibe valor total sem desconto
    print("Valor final: R$ ", valor_Compra)