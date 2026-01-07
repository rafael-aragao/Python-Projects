import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Soma de Números")
root.geometry("300x200")

def somar():
    n1 = int(entrada1.get())
    n2 = int(entrada2.get())
    messagebox.showinfo("Resultado", f"A soma é {n1 + n2}")

entrada1 = tk.Entry(root)
entrada1.pack(pady=5)
entrada2 = tk.Entry(root)
entrada2.pack(pady=5)

btn = tk.Button(root, text="Somar", command=somar)
btn.pack(pady=10)

root.mainloop()