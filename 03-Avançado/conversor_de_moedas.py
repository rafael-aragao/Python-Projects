def real_para_dolar(valor):
    return valor / 5

def real_para_euro(valor):
    return valor / 6

def menu():
    print("1 - Converter para Dólar")
    print("2 - Converter para Euro")

menu()

valor = float(input("Digite o valor em reais: "))
opcao = int(input("Escolha a opção: "))

if opcao == 1:
    print("Dólares:", real_para_dolar(valor))
elif opcao == 2:
    print("Euros:", real_para_euro(valor))
else:
    print("Opção inválida")