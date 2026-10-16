#Exemplo18- Maior ou iguais
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler 2 números e mostrar qual deles é maior ou se são iguais.

#Entrada: Solicita os dois números ao usuário

n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

#Decisão 1: Verifica se o 1° número é maior
if n1 > n2:
    #Saída 1: Mostra que o 1° número e maior e o seu valor
    print(f"O maior é {n1}")
#Decisão 2: Verifica se o 2° número é maior
elif n2 > n1:
    #Saída 2: Mostra que o 2° número é maior
    print(f"O maior é {n2}")
#Caso restante
else:
    print("Os números são iguais")