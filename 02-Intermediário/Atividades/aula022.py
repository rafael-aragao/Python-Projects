import tkinter as tk

janela = tk.Tk()
janela.title("Formulário")
janela.geometry("300x200")

tk.Label(janela, text="Nome").grid(row=0, column=0)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)

tk.Label(janela, text="Idade").grid(row=1, column=0)
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1)

botao = tk.Button(janela, text="Enviar")
botao.grid(row=2, column=0, columnspan=2)

janela.mainloop()