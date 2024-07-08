class Humano:
    def __init__(self, nome, idade, funcao):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        
        
    def andar(self):
        print ("andando...")
        
    def falar(self):
        print("falando...")
    
class Professora(Humano):
    pass


class Aluno(Humano):
    pass

class Diretora(Humano):
    pass

aluno1 = Aluno("Jonas", 28, "")