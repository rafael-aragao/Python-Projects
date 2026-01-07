import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re

def aplicar_mascara(event):
    texto = entrada_cpf.get()
    texto = re.sub(r'\D', '', texto)
    novo_texto = ""

    for i in range(len(texto)):
        if i in [3, 6]:
            novo_texto +='.' 
        elif i == 9:
            novo_texto += '-'
        novo_texto += texto[i]

    entrada_cpf.delete(0, tk.END)
    entrada_cpf.insert(0, novo_texto)

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len (cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int (cpf[9]):
        return False
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf[10]):
        return False
    
    return True
def verificar():
    cpf = entrada_cpf.get()
    if validar_cpf(cpf):
        messagebox.showinfo("Ok", "CPF Válido")
    else:
        messagebox.showinfo("Erro", "CPF Inválido")

root = tk.Tk()
root.title("Validador de CPF")
root.geometry("300x150")

tk.Label(root, text="Digite o CPF: ", font=("Arial", 12)).pack(pady=5)
entrada_cpf = ttk.Entry(root, font=("Arial", 12))
entrada_cpf.pack(pady=5)

entrada_cpf.bind("<KeyRelease>", aplicar_mascara)
tk.Button(root, text="Validar", command=verificar).pack(pady=10)

root.mainloop()