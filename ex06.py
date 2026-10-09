#Exemplo06-Compra na cantina
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler o preço de um lanche, a quantidade comprada e o valor que o cliente pagou
#e mostrar o total da compra e o troco.

#Variavel constante onde armazena o preço do lanche
preco_Coxinha = 4.50

#Entrada: Solicita a quantidade de lanches comprados
quantidade = int(input("Digite a quantidade de lanches comprada: "))

#Processamento: Calcula o total e o troco
total = preco_Coxinha * quantidade
valor_pago = float(input("Digite o valor pago pelo cliente: "))
troco = valor_pago - total

#Saída: Exibe o total da compra e o troco
print("Total: R$ ", total)
print("Troco: R$ ", troco)
