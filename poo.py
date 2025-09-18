#poo
#classe exemplo

class Pessoa:
    def __init__(self, nome, idade) -> None: #construtor
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

#objetos

pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")
print(pessoa1.saudacao())
print(pessoa2.saudacao())

