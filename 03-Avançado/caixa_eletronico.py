def depositar(saldo, valor):
    return saldo + valor

def sacar(saldo, valor):
    if valor > saldo:
        print("Saldo insuficiente")
        return saldo
    else:
        return saldo - valor

def mostrar_saldo(saldo):
    print("Saldo atual:", saldo)

saldo = 0

print("1 - Depositar")
print("2 - Sacar")

opcao = int(input("Escolha uma opção: "))

valor = float(input("Digite o valor: "))

if opcao == 1:
    saldo = depositar(saldo, valor)
elif opcao == 2:
    saldo = sacar(saldo, valor)

mostrar_saldo(saldo)