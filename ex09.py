#Exemplo09- Verificação de Par ou Ímpar
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler um número e verificar se ele é par ou ímpar.

#Entrada: Solicita o número ao usuário
numero = int(input("Digite um número: "))

#Decisão 1: Verifica se o número é par
if numero % 2 == 0:
    #Saída1 : Informa que o número e par
    print("Par")
#Caso restante
else:
    #Saída2: informa que o número é ímpar
    print("Ímpar")