#Exemplo21- Faixa etária
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler a idade de uma pessoa e mostrar a faixa etária.

#Entrada: Solicita  idade ao usuário

idade = int(input("Digite sua idade: "))

#Decisão 1: verifica se a faixa etária e de criança
if idade <= 12:
    #Saída 1 : exibe criança
    print("Criança")
#Decisão 2: verifica se a faixa etária e de adolescente
elif idade <= 17:
    #Saída 2: exibe adolescente
    print("Adolescente")
#Decisão 3: verifica se a faixa etária e de adulto
elif idade <= 59:
    #Saída 3: exibe adulto
    print("Adulto")
#Decisão 4: verifica se a faixa etária e de Idoso
elif idade >= 60:
    #Saída 4: exibe idoso
    print("Idoso")
#Caso restante
else:
    #Saída 5: exibe idade inválida
    print("Idade inválida")