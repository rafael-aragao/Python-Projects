def mostrar_menu():
    print("\n=== SISTEMA DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Remover aluno")
    print("5 - Sair")


def cadastrar_aluno(lista):
    nome = input("Digite o nome do aluno: ")
    lista.append(nome)
    print("Aluno cadastrado com sucesso!")


def listar_alunos(lista):
    if len(lista) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\nLista de alunos:")
        for aluno in lista:
            print("-", aluno)


def buscar_aluno(lista):
    nome = input("Digite o nome para buscar: ")

    if nome in lista:
        print("Aluno encontrado!")
    else:
        print("Aluno não encontrado.")


def remover_aluno(lista):
    nome = input("Digite o nome do aluno para remover: ")

    if nome in lista:
        lista.remove(nome)
        print("Aluno removido.")
    else:
        print("Aluno não encontrado.")


alunos = []

while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno(alunos)

    elif opcao == "2":
        listar_alunos(alunos)

    elif opcao == "3":
        buscar_aluno(alunos)

    elif opcao == "4":
        remover_aluno(alunos)

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")