#personagem classe mae
#heroi classe filha herda de personagem
#inimigo classe filha herda de personagem
import random


class Personagem:
    def __init__(self, nome, vida , nivel) -> None:
        self.__nome = nome #atributo privado __nome
        self.__vida = vida
        self.__nivel = nivel
    #usando privado porque ninguem pode alterar o nome, vida e nivel do personagem diretamente
     # get porque o atributo é privado   
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel()*2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)  # First apply damage to the target
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel) #chama o construtor da classe mae
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou ataque especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"

class Jogo:

    """classe orquestradora do jogo"""
    def __init__(self) -> None:
        self.heroi= Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo= Inimigo(nome="Inimigo", vida=80, nivel=3, tipo="Monstro")
     
    def iniciar_batalha(self):
        print("Batalha iniciada!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha uma ação (1: Ataque normal, 2: Ataque especial): ")


            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida! Escolha 1 ou 2.")
            # inimigo ataca o heroi
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
        if self.heroi.get_vida() > 0:
            print("\nParabéns! Você venceu a batalha!")
        else:
            print("\nVocê foi derrotado.")

# Criar instancias do jogo
jogo = Jogo()
jogo.iniciar_batalha()


heroi = Heroi(nome = "Arqueiro", vida = 100, nivel = 5, habilidade = "Tiro com Arco")
print(heroi.exibir_detalhes())
inimigo = Inimigo(nome = "Goblin", vida = 80, nivel = 3, tipo = "Monstro")
print(inimigo.exibir_detalhes())

