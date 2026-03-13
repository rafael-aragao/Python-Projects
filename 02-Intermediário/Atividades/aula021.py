import tkinter as tk

janela = tk.Tk()
janela.title("Janela formatada")

janela.geometry("400x300")   # tamanho da janela
janela.config(bg="lightblue")  # cor de fundo

texto = tk.Label(janela, text="Minha primeira interface", bg="lightblue", font=("Arial", 16))
texto.pack(pady=100)

janela.mainloop()