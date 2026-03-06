def contador(inicio, fim):
    for i in range(inicio, fim + 1):
        print(i)

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

contador(inicio, fim)