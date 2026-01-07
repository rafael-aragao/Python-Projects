import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

janela = tk.Tk()
janela.title("Rede Social")
janela.geometry("300x200")

def abrir_boas_vindas():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Bem vindo")
    nova_janela.geometry("350x300")

    tk.Label(nova_janela, text="Login realizado com sucesso!", font=("Arial", 12)).pack(pady=10)

    base_dir = os.path.dirname(__file__)
    caminho_imagem = os.path.join(base_dir, "imagens", "perfil.png")

    try:
        imagem = Image.open(caminho_imagem)
        imagem = imagem.resize((120, 120))
        foto = ImageTk.PhotoImage(imagem)

        lbl_imagem = tk.label(nova_janela, image=foto)
        lbl_imagem.image = foto
        lbl_imagem.pack(pady=10)
    except FileNotFoundError:
        tk.Label(nova_janela, text="Imagem não encontrada", fg="red").pack(pady=10)
        tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy).pack(pady=10)

def verificar_login():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    if usuario == "Rafael" and senha == "1234":
        abrir_boas_vindas()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

tk.Label(janela, text="Usuário: ").pack(pady=10)
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack(pady=5)

tk.Label(janela, text="Senha: ").pack(pady=10)
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack(pady=5)

btn_login = tk.Button(janela, text="Entrar", command=verificar_login)
btn_login.pack(pady=10)

janela.mainloop()