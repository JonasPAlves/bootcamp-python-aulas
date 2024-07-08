class Pai:
    def __init__(self, nome, idade, qtd_filhos):
        self.nome = nome
        self.idade = idade
        self.qtd_filhos = qtd_filhos
        
        
    def cuidar(self):
        print ("Vai cuidar do menino")
        

p1 = Pai("Jonas", "27", "3")

p1.cuidar()