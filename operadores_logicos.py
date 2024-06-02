# and para ser True todas as situações devem ser verdadeiras
# or pelo menos uma das situações devem ser verdadeiras
"""print (True and True)
print (True or True)
print (True or False)
print (False and False)
print (False or False)"""

saldo = 100
saque = 200
limite = 120
conta_especial = True
mensagem = "Ok"

exp1 = (saldo >= saque and saque <= limite) and (conta_especial and saldo >= saque)
print (exp1)

exp2 = (saldo >= saque and saque <= limite) or (saldo >= saque or saque <= limite)
print (exp2)

not saque >= saldo ## negação


if (saldo > saque):

    print ("Ok, saque realizado")

else:
    print("Saldo insuficiente!")