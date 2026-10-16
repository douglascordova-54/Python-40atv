#Exemplo15- Dia da semana
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler um número de 1 a 7 e mostrar o dia da semana correspondente(1= Domingo... e aí em diante)
#Para qualquer outro número exibir dia inválido

#Entrada: Solicita o número ao usuário

dia = int(input("Digite um número de 1 a 7: "))

#Decisão 1: verifica se o número digitado corresponde a domingo
if dia == 1:
    #Saída 1: exibe domingo
    print("Domingo")
#Decisão 2: verifica se o número digitado corresponde a segunda-feira
elif dia == 2:
    #Saída 2: exibe segunda
    print("Segunda-feira")
#Decisão 3: verifica se o número digitado corresponde a terça
elif dia == 3:
    #Saída 3: exibe terça
    print("Terça-feira")
#Decisão 4: verifica se o número digitado corresponde a quarta
elif dia == 4:
    #Saída 4: exibe quarta
    print("Quarta-feira")
#Decisão 5: verifica se o número digitado corresponde a quinta
elif dia == 5:
    #Saída 5: exibe quinta
    print("Quinta-feira")
#Decisão 6: verifica se o número digitado corresponde a sexta
elif dia == 6:
    #Saída 6: exibe sexta
    print("Sexta-feira")
    #Decisão 7: verifica se o dia correspondente a sábado
elif dia == 7:
    #Saída 7:
    print("Sábado")
#Caso restante
else:
    #Saída 7: exibe Dia inválido
    print("Dia inválido")
