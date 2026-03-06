import random

def jogar_dado():
    return random.randint(1, 6)

def mostrar_resultado(numero):
    print("O dado caiu em:", numero)

resultado = jogar_dado()
mostrar_resultado(resultado)