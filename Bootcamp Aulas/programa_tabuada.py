print("TABUADA com Python.")
num = int ( input("\nDigite um número inteiro para ver sua tabuada: "))
print("\nA tabuada de", num, "será apresentada abaixo:")
print(20*"-")
for i in range (11):
  print(num, i, num*i)
print(20*"-")