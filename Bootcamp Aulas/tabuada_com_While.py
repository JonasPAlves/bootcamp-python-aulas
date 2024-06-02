opcao= -1

print("\nTABUADA com Python.")
while opcao != 0:
    opcao = int(input("[1] Digitar um número \n[0] Sair \n: "))
    
    if opcao ==1:
        num = int ( input("\nDigite um número inteiro para ver sua tabuada: "))
    print("\nA tabuada de", num, "será apresentada abaixo:")
    print(20*"-")
    for i in range (11):
        print("{} x {} = {:2}".format(num,i,num*i))
    print(20*"-")
    
else:
    print("Obrigado por utilizar nossos serviços!")
