def verificar_par(num):
    if num % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

numero = int(input("Digite um número: "))
verificar_par(numero)