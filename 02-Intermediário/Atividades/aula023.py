import tkinter as tk

janela = tk.Tk()
janela.title("Janela fixa")

janela.geometry("400x250")

botao = tk.Button(janela, text="Clique aqui")
botao.pack(expand=True)

janela.mainloop()