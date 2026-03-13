import tkinter as tk

def somar():
    a = float(entrada1.get())
    b = float(entrada2.get())
    resultado.config(text="Resultado: " + str(a + b))

def subtrair():
    a = float(entrada1.get())
    b = float(entrada2.get())
    resultado.config(text="Resultado: " + str(a - b))

def multiplicar():
    a = float(entrada1.get())
    b = float(entrada2.get())
    resultado.config(text="Resultado: " + str(a * b))

def dividir():
    a = float(entrada1.get())
    b = float(entrada2.get())
    resultado.config(text="Resultado: " + str(a / b))

# Criar janela
janela = tk.Tk()
janela.title("Calculadora")

# Campos de entrada
tk.Label(janela, text="Primeiro número").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Segundo número").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

# Botões
tk.Button(janela, text="Somar", command=somar).pack()
tk.Button(janela, text="Subtrair", command=subtrair).pack()
tk.Button(janela, text="Multiplicar", command=multiplicar).pack()
tk.Button(janela, text="Dividir", command=dividir).pack()

# Resultado
resultado = tk.Label(janela, text="Resultado:")
resultado.pack()

# Executar janela
janela.mainloop()