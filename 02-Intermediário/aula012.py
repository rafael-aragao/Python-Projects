import getpass
usuario_correto = "CutchVerse"
senha_correta = "spaceyeeter123"

usuario = input("Digite o usuário: ")
senha = getpass.getpass("Digite a senha: ")

#Validação

if usuario == usuario_correto and senha == senha_correta:
    print("Acesso Liberado")
else: 
    print("Acesso Negado")