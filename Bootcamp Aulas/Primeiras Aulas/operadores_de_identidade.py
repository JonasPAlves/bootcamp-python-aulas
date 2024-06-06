curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

verifica = (curso is nome_curso)
print(verifica)

verifica = (curso is not nome_curso)
print(verifica)