import tkinter as tk

def mostrar_nome():
    nome = entrada.get()
    resultado.config(text="Olá, " + nome)

janela = tk.Tk()
janela.title("Entrada de dados")

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Mostrar", command=mostrar_nome)
botao.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()