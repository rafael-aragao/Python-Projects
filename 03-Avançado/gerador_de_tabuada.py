def titulo():
    print("=== GERADOR DE TABUADA ===")

def mostrar_tabuada(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

titulo()

num = int(input("Digite um número: "))

mostrar_tabuada(num)