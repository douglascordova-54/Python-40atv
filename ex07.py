#Exemplo07-Maior ou menor de idade
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler a idade de uma pessoa e informar se ela é maior de idade ou menor.

#Entrada: Solicita a idade da pessoa
idade = int(input("Digite sua idade:"))

#Decisão 1: Verifica se a idade é maior ou igual a 18 anos
if idade >= 18:
    #Saída 1: exibe a mensagem innformando que a pessoa é maior de idade
    print("Maior de idade")
#Caso restante
else:
    #Saída 2: exibe a mensagem innformando que a pessoa é menor de idade
    print("Menor de idade")