menu =  '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite= 500
extrato = ""
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        num =float (input("Qual valor você deseja depositar? "))
        if (num > 0):
            saldo += num
            extrato += f"Depósito: R$ {num:.2f}\n"
        else: 
            print("Por favor digite um valor maior que zero!")
    
    elif opcao == "s":
        if (LIMITE_SAQUE<1):
            print(f"Seu limite de saques por dia esgotou! Favor sacar amanhã! ")
        else: saque =float (input("Qual valor você deseja sacar? "))
        
        if(saque < 0):
            print("Por favor digite um valor maior que zero!")
        elif (saque > saldo):
            print("Saldo insuficiente. Favor depositar!")
            
        elif(saque > limite):
            print("Seu limite de Saque por operação é de R$ 500")
        
        elif (LIMITE_SAQUE<1):
            print()
                        
        else: 
            print(f"Sacando o valor de: R$ {saque:.2f}...\n")
            saldo  -= saque
            LIMITE_SAQUE += -1
            extrato += f"Saque: R$ {saque:.2f}\n"
               
    elif opcao == "e":
        print("\n=========== EXTRATO ===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("ESTE É SEU EXTRATO!")
        print(f"Saldo: R$ {saldo:.2f}")
        print("======================")
        
    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema!")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
            
 
 
