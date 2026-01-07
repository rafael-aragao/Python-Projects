import tkinter as tk

def mostrar_nome():
    nome = entrada.get()
    mensagem_label.config(text=f"Olá {nome}!")

janela = tk.Tk()
janela.title("Mensagem com nome")
janela.geometry("300x200")
 
tk.Label(janela, text="Digite seu nome:").pack(pady=5)

entrada = tk.Entry(janela)
entrada.pack(pady=5)

botao = tk.Button(janela, text="Enviar", command=mostrar_nome)
botao.pack(pady=5)

mensagem_label = tk.Label(janela, text="", font=("Arial", 12))
mensagem_label.pack(pady=10)
janela.mainloop()