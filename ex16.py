#Exemplo16- Saque no caixa eletrônico
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler o saldo da conta e o valor que a pessoa quer sacar. Se houver saldo suficiente e mostre o novo saldo
#Caso contrario mostre saldo insuficiente.

#Entrada: Solicita o saldo da conta e o valor do saque
saldo = float(input("Digite o saldo da conta: "))
valor_Saque = float(input("Digite o valor do saque: "))

#Processamento: Cálculo do saldo restante após o saldo
resto_saldo = saldo - valor_Saque

#Decisão 1: Verifica se o saldo é suficiente para realizar o saque
if saldo >= valor_Saque:
    #Saída 1: Mostra que o saque foi realizado e a quantia restante de saldo na conta
    print("Saque realizado. Novo saldo: R$ ",resto_saldo)
#Caso restante
else:
    #Saída 2: Mostra que o saldo é insuficiente para o saque
    print("Saldo insuficiente")
    
