import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Atalho")
root.geometry("300x150")

def acao():
    messagebox.showinfo("Atalho", "Botão ativado pelo atalho Ctrl+S!")

btn = tk.Button(root, text="Salvar (Ctrl+S)", command=acao)
btn.pack(pady=40)

root.bind("<Control-s>", lambda event: acao())

root.mainloop()