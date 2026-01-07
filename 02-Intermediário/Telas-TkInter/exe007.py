import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Lista de Frutas")
janela.geometry("250x200")

def mostrar_selecionado():
    fruta = lista.get(lista.curselection())
    messagebox.showinfo("Selecionado", f"Você escolheu {fruta}")

lista = tk.Listbox(janela)
frutas = ["Maçã", "Banana", "Laranja", "Morango"]
for f in frutas:
    lista.insert(tk.END, f)
lista.pack(pady=10)

btn = tk.Button(janela, text="Escolher", command=mostrar_selecionado)
btn.pack()

janela.mainloop()