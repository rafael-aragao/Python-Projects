import tkinter as tk

janela = tk.Tk()
janela.title("Minha primeira janela")
janela.geometry("300x200")

label = tk.Label(janela, text="Olá Mundo", font=("Arial", 14))
label.pack(pady=20)

botao = tk.Button(janela, text="Fechar", command=janela.destroy)
botao.pack(pady=10)

janela.mainloop()