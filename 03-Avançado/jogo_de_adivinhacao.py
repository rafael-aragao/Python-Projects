import random

def gerar_numero():
    return random.randint(1, 10)

def verificar_palpite(numero, palpite):
    if palpite == numero:
        return "Acertou!"
    elif palpite < numero:
        return "Tente um número maior"
    else:
        return "Tente um número menor"

def jogar():
    numero = gerar_numero()
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    resultado = verificar_palpite(numero, palpite)
    print(resultado)

jogar()