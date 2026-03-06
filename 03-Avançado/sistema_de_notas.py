def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def mostrar_resultado(nome, media, situacao):
    print("Aluno:", nome)
    print("Média:", media)
    print("Situação:", situacao)

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)
situacao = verificar_situacao(media)

mostrar_resultado(nome, media, situacao)