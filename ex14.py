#Exemplo14- Radar de velocidade
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler a velocidade de um carro. Caso passar do limete de 80 km/h
#Mostrar a quantos km/h ele estava.

#Entrada: Solicita a velocidade ao usuário
velocidade = int(input("Digite a velocidade do carro: "))

#Processamento: Calcula quanto o motorista ultrapassou o limite
ultrapassouu = velocidade - 80

#Decisão 1: Verifica se a velocidade é maior que 80 km/h
if velocidade > 80:
    #Saída 1: exibe mensagem de multado e o quanto ultrapassou o limite
    print("multado! Você passou", ultrapassouu, "km/h do limite.")
#Caso restante
else:
    #Saída 2: mostra mensagem de boa viagem
    print("Velocidade dentro do limite. Boa viagem!")
