def tabuada(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

n = int(input("Digite um número: "))
tabuada(n)