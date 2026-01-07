import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Checkbutton")
janela.geometry("300x150")

def verificar():
    if var.get()== 1:
        messagebox.showinfo("Status", "Você marcou a opção")
    else:
        messagebox.showinfo("Status", "Você não marcou a opção")
var = tk.IntVar()
check = tk.Checkbutton(janela, text="Clique aqui", variable=var)
check.pack(pady=20)

btn = tk.Button(janela, text="Verificar", command=verificar)
btn.pack()

janela.mainloop()