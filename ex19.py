#Exemplo19- Situação do aluno
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler duas notas, calcular a média e mostrar situação do aluno.

#Entrada: Solicita as notas 

nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))

#Processamento:Calcula a média e mostra a situação
media = (nota1 + nota2) / 2

#Decisão 1: verifica se o aluno está aprovado
if media >= 7:
    #Saída 1: exibe aprovado
    input("Aprovado")
#Decisão 2: verifica se aluno está reprovado
elif media < 5:
    #Saída 2: exibe reprovado
    print("Reprovado")
#Caso restante
else:
    #Saída 3: mostra que o aluno está de recuperação
    print("Recuperação")