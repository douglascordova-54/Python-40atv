#Exemplo05-Transformando minutos em horas
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler uma quantidade de minutos e mostrar quantas horras e minutos ela representa.

#Entrada: Solicita a quantidade de minutos
minutos = int(input("Digite a quantidade de minutos: "))

#Processamento: Calcula a quantidade de horas e minutos
horas = minutos // 60
minutos_Restantes = minutos % 60

#Saída: Exibi a quantidade de horas e minutos convertidas
print(horas, "hora(s) e ",minutos_Restantes, "minuto(s)" )