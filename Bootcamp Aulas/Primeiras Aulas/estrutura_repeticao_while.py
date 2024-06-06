opcao = -1

while opcao != 0: # != sinal de diferente
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 1:
        print("Sacando...")
    elif opcao ==2:
        print("Exibindo o  Extrato...")
    
    else:
        print("Obrigado por ser nosso cliente! ")
        
while True: # loop infinito pois sempre será verdadeiro até que tenha uma condição para encerrar o loop
    numero = pcao = int(input("Informe um número: "))
    
    if numero ==10:
        break # condição para parar o loop
    print (numero)
    
for numero in  range(100):
    
    if numero % 2 == 0: # se número dividido por 2 for igual a 0 | números primos
        continue
    
    print (numero, end=" ")
        
    