# encapsulamento, herança, polimorfismo e abstração

#herança

print("\n Exemplo de herança")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        return f"{self.nome} está andando."
    
    def emitir_som(self):
        pass
    
class Cachorro(Animal): # herdou de Animal
    def emitir_som(self):
        return "Au Au"

class Gato(Animal): # herdou de Animal
    def emitir_som(self):
        return "Miau Miau"


dog = Cachorro("Rex")
cat = Gato("Mimi")

print ("\n Exemplo de polimorfismo")
animais = [dog, cat]
for animal in animais:
    print(f"{animal.nome} diz: {animal.emitir_som()}")

print("\n Exemplo de encapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo  # atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado. Novo saldo: {self.__saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.__saldo}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def ver_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(1000)
conta.ver_saldo()
conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)  # tentativa de saque maior que o saldo
conta_aline = ContaBancaria(3000)
conta_aline.ver_saldo()
conta_aline.depositar(1500)
conta_aline.sacar(1000)


print("\n Exemplo de abstração")
from abc import ABC, abstractmethod # Abstract Base Class
class Veiculo (ABC):
    @abstractmethod # decorador
    def acelerar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    
    
class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    def acelerar(self):
        return "Carro ligado"
    def desligar(self):
        return "Carro desligado"
volvo = Carro()
print(volvo.acelerar())
print(volvo.desligar())

"""exemplo quando se pede pra mudar de mysql para mongo db, so muda a classe de conexao, 
se tiver classe abstrata, o resto do codigo nao precisa mudar"""