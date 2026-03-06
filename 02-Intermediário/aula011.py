numero = int(input("Digite um numero entre 1 e 3: "))

match numero:
    case 1:
        print("Você escolheu domingo")
    case 2:
        print("Você escolheu segunda-feira")
    case 3:
        print("Você escolheu sábado")