from typing import Any


def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de chamar a função.")
        resultado = func(*args, **kwargs)
        print("Depois de chamar a função.")
        return resultado
    return wrapper #embrulho

@meu_decorador
def minha_funcao():
    print("Minha funcao está sendo executada.")

# muito utilizado em validações, autenticações, logs

minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
    
    def __call__(self) -> Any:
        print("Antes da funcao ser chamada (decorador de classe).")
        self.func()
        print("Depois da funcao ser chamada (decorador de classe).")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao está sendo executada.")

segunda_funcao()
