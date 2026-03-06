def cadastrar_aluno(lista):
    nome = input("Digite o nome do aluno: ")
    lista.append(nome)

def mostrar_alunos(lista):
    print("Lista de alunos:")
    for aluno in lista:
        print(aluno)

alunos = []

for i in range(3):
    cadastrar_aluno(alunos)

mostrar_alunos(alunos)