import tkinter as tk

janela = tk.Tk()
janela.title("Minha primeira janela")

texto = tk.Label(janela, text="Olá, mundo!")
texto.pack()

janela.mainloop()