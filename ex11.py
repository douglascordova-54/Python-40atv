#Exemplo11- O maior de dois números
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler dois números diferentes e mostrar quel é o maior.

#Entrada: Solicita os números ao usuário
n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

#Decisão 1: Verifica se 1° número e maior que o 2° número
if n1 > n2:
    #Saída1: exibe que o 1° número é maior
    print("O maior é", n1)
#Caso restante    
else:
    #Saída2: exibe que 2° número é maior
    print("O maior é", n2)
    