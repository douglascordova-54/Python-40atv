#Exemplo17- positivo negativo ou zero
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler um número e informar se ele positivo negativ ou zero

#Entrada: Solicita o número ao usuário

num = int(input("Digite um número: "))

#Decisão 1: verifica se o número é positivo
if num > 0:
    #Saída 1: exibe que é positivo
    print("Positivo")
#Decisão 2 : Verifica se é negativo
elif num < 0:
    #Saída 2: exibe que é negativo
    print("Negativo")
#Caso restante
else:
    #Saída 3: exibe que é zero
    print("Zero")
