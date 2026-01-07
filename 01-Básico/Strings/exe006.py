frase = input("Digite a frase: ")
print("Escolha uma opção: ")
print("1 - upper() ")
print("2 - lower() ")
print("3 - capitalize")
op = input("Opção ")

if op == "1":
    print(frase.upper())
elif op == "2":
    print(frase.lower())
elif op == "3":
    print(frase.capitalize())
else:
    print("Opção Inválida")