# @classmethod
# @staticmethod




class MinhaClasse:
    valor = 10  # atributo de classe
    def __init__(self, nome) -> None:
        self.nome = nome
    # requer uma instância da classe como primeiro argumento
    def metodo_de_instancia(self):
        return f"Olá, {self.nome}! Este é um método de instância."


    @classmethod #recebe a referência da classe como primeiro argumento
    def metodo_de_classe(cls):
        return f"Este é um método de classe. Valor da classe: {cls.valor}"
    
    @staticmethod #nao recebe nem a instância nem a classe como primeiro argumento
    def metodo_estatico():
        return "Este é um método estático. Não tem acesso à instância ou à classe."


obj = MinhaClasse("Aline")
print(obj.metodo_de_instancia())  # Saída: Olá, Aline!
print(MinhaClasse.valor)  # Saída: 10
print(MinhaClasse.metodo_de_classe())  # Saída: Este é um método de classe. Valor da classe: 10
print(MinhaClasse.metodo_estatico())  # Saída: Este é um método está

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    

configuracao1 = "Toyota,Corolla,2020"
carro1 = Carro.criar_carro(configuracao1)
print(f"Carro 1: {carro1.marca} \nModelo: {carro1.modelo} \nAno: {carro1.ano}")

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
print(Matematica.somar(5, 3))  # Saída: 8
print(Matematica.multiplicar(5, 3))  # Saída: 15