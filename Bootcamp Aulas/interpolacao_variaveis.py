nome = "Jonas"
idade = 27
profissao = "Programador"
linguagem = "Python"

# Jeito antigo de interpolar as variáveis - não é recomendado!
print("Olá, eu me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no Curso de %s." 
      % (nome, idade, profissao, linguagem))
#%s - significa que é uma String
#%d - significa que é um Inteiro
#%f - significa que é um Float

# Método format!
print("Olá, eu me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no Curso de {}." 
      .format (nome, idade, profissao, linguagem))

# Método format mais sofisticado!
print("Olá, eu me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no Curso de {linguagem}." 
      .format (nome=nome, idade= idade, profissao=profissao, linguagem=linguagem))

# Método f-string RECOMENDADO!
print(f"Olá, eu me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no Curso de {linguagem}.")