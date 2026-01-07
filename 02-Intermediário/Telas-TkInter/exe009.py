import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Cadastro")
janela.geometry("300x200")

def abrir_boas_vindas():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Bem vindo")
    nova_janela.geometry("300x150")

    tk.Label(nova_janela, text="Login Realizado com sucesso", font=("Arial", 12)).pack(pady=20)
    tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy).pack(pady=10)

def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "admin" and senha == "1234":
        abrir_boas_vindas()
    else:
        messagebox.showerror("Erro", "Usuario ou senha incorreta")

tk.Label(janela, text="Usuario: "  ).pack(pady=10)
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=20)

tk.Label(janela, text="Senha: ").pack(pady=10)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack(pady=20)

btn_login = tk.Button(janela, text="Entrar", command=verificar_login)
btn_login.pack(pady=10)

janela.mainloop()