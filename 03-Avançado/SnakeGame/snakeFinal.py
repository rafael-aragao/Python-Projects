# Snake Game
import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice
import os

pygame.init()

# -------------------------
# CAMINHO DA PASTA DO JOGO
# -------------------------
pasta_jogo = r"C:\Users\Aluno-30\Documents\Prof_Rafael\Python\Turma_Sab_09h00m"

# -------------------------
# MÚSICA E SOM
# -------------------------
pygame.mixer.music.set_volume(0.5)

# Coloque aqui o nome real da música
pygame.mixer.music.load(os.path.join(pasta_jogo, "time_for_adventure.mp3"))
pygame.mixer.music.play(-1)

# Coloque aqui o nome real do som da colisão
som_colisao = pygame.mixer.Sound(os.path.join(pasta_jogo, "coin.wav"))
som_colisao.set_volume(0.7)

# -------------------------
# TELA
# -------------------------
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")
relogio = pygame.time.Clock()

# -------------------------
# IMAGENS
# -------------------------

# Imagem da cabeça da cobra
imagem_cobra = pygame.image.load(os.path.join(pasta_jogo, "cobra.png"))
imagem_cobra = pygame.transform.scale(imagem_cobra, (20, 20))

# Imagens das frutas
imagens_frutas = [
    pygame.image.load(os.path.join(pasta_jogo, "maca.png")),
    pygame.image.load(os.path.join(pasta_jogo, "abacaxi.png")),
    pygame.image.load(os.path.join(pasta_jogo, "morango.png")),
    pygame.image.load(os.path.join(pasta_jogo, "laranja.png"))
]

# Redimensiona todas as frutas para 20x20
imagens_frutas = [
    pygame.transform.scale(img, (20, 20)) for img in imagens_frutas
]

# Escolhe uma fruta inicial aleatória
imagem_snack = choice(imagens_frutas)

# -------------------------
# VARIÁVEIS DO JOGO
# -------------------------
x_player = largura / 2
y_player = altura / 2

velocidade = 10

x_controle = velocidade
y_controle = 0

x_snack = randint(40, 600)
y_snack = randint(50, 430)

Pontos = 0
comprimento_inicial = 5
lista_corpo = []
perdeu = False

cores = {
    "branco": (255, 255, 255),
    "vermelho": (255, 0, 0),
    "preto": (0, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarelo": (255, 255, 0)
}

fonte = pygame.font.SysFont("MINECRAFT PE", 30, True, False)


# -------------------------
# FUNÇÃO PARA DESENHAR O CORPO
# -------------------------
def aumentar_corpo(lista_corpo):
    for XeY in lista_corpo[:-1]:
        pygame.draw.rect(tela, cores["verde"], (XeY[0], XeY[1], 20, 20))


# -------------------------
# FUNÇÃO PARA REINICIAR O JOGO
# -------------------------
def reiniciar_jogo():
    global Pontos, comprimento_inicial
    global x_player, y_player
    global lista_corpo
    global x_snack, y_snack
    global perdeu
    global x_controle, y_controle
    global imagem_snack

    Pontos = 0
    comprimento_inicial = 5

    x_player = largura / 2
    y_player = altura / 2

    x_controle = velocidade
    y_controle = 0

    lista_corpo = []

    x_snack = randint(40, 600)
    y_snack = randint(50, 430)

    imagem_snack = choice(imagens_frutas)

    perdeu = False


# -------------------------
# LOOP PRINCIPAL
# -------------------------
while True:
    relogio.tick(30)
    tela.fill(cores["preto"])

    pontuacao = f"Pontos: {Pontos}"
    renderizacao = fonte.render(pontuacao, True, cores["branco"])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:

            # Tecla A - esquerda
            if event.key == K_a:
                if x_controle != velocidade:
                    x_controle = -velocidade
                    y_controle = 0

            # Tecla D - direita
            if event.key == K_d:
                if x_controle != -velocidade:
                    x_controle = velocidade
                    y_controle = 0

            # Tecla W - cima
            if event.key == K_w:
                if y_controle != velocidade:
                    y_controle = -velocidade
                    x_controle = 0

            # Tecla S - baixo
            if event.key == K_s:
                if y_controle != -velocidade:
                    y_controle = velocidade
                    x_controle = 0

    # Movimenta a cobra
    x_player = x_player + x_controle
    y_player = y_player + y_controle

    # Cria o retângulo da cabeça para colisão
    player = pygame.Rect(x_player, y_player, 20, 20)

    # Cria o retângulo da fruta para colisão
    snack = pygame.Rect(x_snack, y_snack, 20, 20)

    # Desenha a fruta aleatória
    tela.blit(imagem_snack, (x_snack, y_snack))

    # Verifica colisão com a fruta
    if player.colliderect(snack):
        x_snack = randint(40, 600)
        y_snack = randint(50, 430)

        # Escolhe outra fruta aleatória
        imagem_snack = choice(imagens_frutas)

        Pontos = Pontos + 1
        som_colisao.play()
        comprimento_inicial = comprimento_inicial + 1

    # Lista com posição da cabeça
    lista_cabeca = []
    lista_cabeca.append(x_player)
    lista_cabeca.append(y_player)

    # Adiciona cabeça na lista do corpo
    lista_corpo.append(lista_cabeca)

    # Verifica colisão com o próprio corpo
    if lista_corpo.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont("MINECRAFT PE", 20, True, True)
        mensagem = "Game Over! Aperte a tecla R para reiniciar"
        renderizacao2 = fonte2.render(mensagem, True, cores["vermelho"])
        perdeu = True

        while perdeu:
            tela.fill(cores["preto"])

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            tela.blit(renderizacao2, (80, altura // 2))
            pygame.display.update()

    # Limita o tamanho do corpo
    if len(lista_corpo) > comprimento_inicial:
        del lista_corpo[0]

    # Desenha o corpo
    aumentar_corpo(lista_corpo)

    # Desenha a cabeça com imagem
    tela.blit(imagem_cobra, (x_player, y_player))

    # Mostra pontuação
    tela.blit(renderizacao, (400, 40))

    pygame.display.update()