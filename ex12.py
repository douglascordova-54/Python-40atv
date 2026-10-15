#Exemplo12- Divisão segura
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler dois números:dividendo e divisor.Se o divisor for zero
#Mostrar mensagem de erro.

#Entrada: Solicita os números ao usuário
dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

#Decisão 1: Verifica se o divisor será diferente de zero
if divisor != 0:
    #Procesamento: realiza a divisão
    resultado = dividendo/divisor
    #Saída 1: exibe o resultado da divisão
    print("Resultado: ",resultado)
#Caso restante
else:
    #Saída 2: exibe a mensagem de erro
    print("Erro: não existe divisão por zero")
    