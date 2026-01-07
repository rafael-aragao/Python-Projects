import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Entrada de Nome")
janela.geometry("350x150")

def rafael():
    nome = entrada.get()
    messagebox.showinfo("Saudação", f"Olá, {nome}!")

entrada = tk.Entry(janela)
entrada.pack(pady=20)

btn = tk.Button(janela, text="Enviar", command=rafael)
btn.pack(pady=10)

janela.mainloop()