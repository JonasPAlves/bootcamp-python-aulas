texto = input("Informe um text: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="") # o texto aparecerá verticalizado!
        
else:
    print()
    print("Fim do programa!")