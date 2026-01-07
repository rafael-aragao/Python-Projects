a = [20, 40, 60]
b = [2, 5, 7]

divisao = []

for i in range(len(a)):
    if b[i] != 0:
        divisao.append(a[i] / b[i])
    else:
        divisao.append("Erro: divisão por zero")
print("Resultado da divisão é: ", divisao)