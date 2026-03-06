def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("Maior número:", maior_numero(n1, n2))