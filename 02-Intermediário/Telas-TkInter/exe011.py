import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

def criar_banco():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE,
            senha TEXT
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar_usuario(usuario, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    try:
        senha_hash = hashlib.md5(senha.encode()).hexdigest()
        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
                       (usuario, senha_hash))
        conn.commit()
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Usuário já existe.")
    conn.close()

def verificar_login(usuario, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?",
                   (usuario, senha_hash))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def tela_login():
    def logar():
        user = entry_user.get()
        pwd = entry_pwd.get()
        if verificar_login(user, pwd):
            messagebox.showinfo("Login", f"Bem-vindo, {user}!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def abrir_cadastro():
        janela_login.destroy()
        tela_cadastro()

    janela_login = tk.Tk()
    janela_login.title("Login")
    janela_login.geometry("300x200")

    tk.Label(janela_login, text="Usuário:").pack(pady=5)
    entry_user = tk.Entry(janela_login)
    entry_user.pack()

    tk.Label(janela_login, text="Senha:").pack(pady=5)
    entry_pwd = tk.Entry(janela_login, show="*")
    entry_pwd.pack()

    tk.Button(janela_login, text="Entrar", command=logar).pack(pady=10)
    tk.Button(janela_login, text="Cadastrar", command=abrir_cadastro).pack()

    janela_login.mainloop()

def tela_cadastro():
    def cadastrar():
        user = entry_user.get()
        pwd = entry_pwd.get()
        if user and pwd:
            cadastrar_usuario(user, pwd)
            janela_cadastro.destroy()
            tela_login()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    janela_cadastro = tk.Tk()
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("300x200")

    tk.Label(janela_cadastro, text="Novo Usuário:").pack(pady=5)
    entry_user = tk.Entry(janela_cadastro)
    entry_user.pack()

    tk.Label(janela_cadastro, text="Senha:").pack(pady=5)
    entry_pwd = tk.Entry(janela_cadastro, show="*")
    entry_pwd.pack()

    tk.Button(janela_cadastro, text="Cadastrar", command=cadastrar).pack(pady=10)

    janela_cadastro.mainloop()

criar_banco()
tela_login()