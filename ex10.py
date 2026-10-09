#Exemplo10- Verifica se está aprovado ou reprovado
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler duas notas de um aluno e calcule a média
#Mostrar se o aluno esta aprovado ou reprovado

#Entrada: Solicita as notas ao usuário
nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))

#Processameto: Calcula média das duas notas
media = (nota1 + nota2) /2

#Decisão 1: Verifica se a média é maior ou igual a 7 e informa se o aluno esta aprovado
if media >= 7:
    #Saída 1:Exibe aprovado
    print("Aprovado")
