#Exemplo13- Senha de acesso
#Aluno: Douglas William de Lima Cordova
#Objetivo: Ler a senha digitada caso correta mostrar acesso liberado. Caso a senha for incorreta
#mostrar acesso negado.

#Entrada: Solicita a senha ao usuário
senha = input("Digite a senha de acesso:")

#Decisão 1: Verifica se a senha digitada está correta
if senha == "senai2026":
    #Saída 1: exibe acesso liberado
    print("Acesso liberado")
#Caso restante
else:
    #Saída 2:exibe acesso negado
    print("Acesso negado")
    

