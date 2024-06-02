
#for numero in range(0,10): # percorre os números do zero ao 9
 #   print(numero) # O texto será Horizontal 
 #   print(numero, end=" ") #end " " é para que o texto seja vertical 
    
    
    #tabuada do 1 ao 10:

print("TABUADA com Python.")
num = int ( input("\nDigite um número inteiro para ver sua tabuada: "))
print("\nA tabuada de", num, "será apresentada abaixo:")
print(20*"-")
for i in range (11):
  print(num, i, num*i)
print(20*"-")