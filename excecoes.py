print("Exemplo de captura de exceções")

try:    
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"O resultado é {resultado}")
    
    
import math

raiz_quadrada = math.sqrt(16)
print(f"A raiz quadrada de 16 é {raiz_quadrada}")