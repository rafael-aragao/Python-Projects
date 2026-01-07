import tkinter as tk
import random

# Função para iniciar o jogo
def iniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    label_resultado.config(text="Digite um número entre 1 e 100")
    entrada.delete(0, tk.END)

# Função para verificar o palpite
def verificar_palpite():
    global tentativas

    try:
        palpite = int(entrada.get())
        tentativas += 1

        if palpite < numero_secreto:
            label_resultado.config(text="⬇Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            label_resultado.config(text="⬆Muito alto! Tente novamente.")
        else:
            label_resultado.config(
                text=f" Parabéns! Acertou em {tentativas} tentativa(s)!"
            )
    except ValueError:
        label_resultado.config(text=" Digite um número válido!")

# ----- Interface gráfica usando TkInter -----
janela = tk.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("400x300")
janela.resizable(False, False)

# Título
label_titulo = tk.Label(janela, text="Adivinhe o Número!", font=("Arial", 18))
label_titulo.pack(pady=10)

# Caixa de entrada
entrada = tk.Entry(janela, font=("Arial", 14), justify="center")
entrada.pack(pady=10)

# Botão de verificar
btn_verificar = tk.Button(
    janela, text="🔍 Verificar", font=("Arial", 12), command=verificar_palpite
)
btn_verificar.pack(pady=5)

# Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Botão de jogar novamente
btn_reiniciar = tk.Button(
    janela, text="Jogar Novamente", font=("Arial", 10), command=iniciar_jogo
)
btn_reiniciar.pack(pady=5)

# Rodapé
label_credito = tk.Label(
    janela, text="Desenvolvido por Rafael Aragão", font=("Arial", 9), fg="gray"
)
label_credito.pack(side="bottom", pady=5)

# Inicia o jogo na primeira vez
iniciar_jogo()

janela.mainloop()
