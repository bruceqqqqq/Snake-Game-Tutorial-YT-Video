import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
######

import pygame
from random import randrange

pygame.init()

# CORES
white, black = (255,255,255), (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# TAMANHO LARGURA ALTURA FUNDO FPS TITULO

largura = 320
altura = 280
tamanho = 10
relogio = pygame.time.Clock()
background = pygame.display.set_mode(size=(largura, altura))
pygame.display.set_caption("SNAKE GAME")


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    background.blit(texto1, [x, y])


def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(background, white, [XY[0], XY[1], tamanho, tamanho])


def maca(maca_x, maca_y):
    pygame.draw.rect(background, red, [maca_x, maca_y, tamanho, tamanho])


def jogo():
    exit = True
    fimdejogo = False
    pontos = 0
    pos_x = randrange(0, largura - tamanho,10) # 0 até 630
    pos_y = randrange(0, altura - tamanho, 10)   # 0 até 630
    maca_x = randrange(0, largura - tamanho,10)  # 0 até 630
    maca_y = randrange(0, altura - tamanho - 40, 10)  # 0 até 630
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    CobraComp = 1
    while exit:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = False
                    fimdejogo = False
                # Eventos com Mouse na tela de Game Over
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        exit = True
                        fimdejogo = False
                        pos_x = randrange(0, largura - tamanho, 10)  # 0 até 630
                        pos_y = randrange(0, altura - tamanho, 10)  # 0 até 630
                        maca_x = randrange(0, largura - tamanho, 10)  # 0 até 630
                        maca_y = randrange(0, altura - tamanho - 40, 10) # 0 até 630
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        exit = False
                        fimdejogo = False

            # Tela de Game Over
            background.fill(black)
            texto("GAME OVER!", red, 50, 45, 30)
            texto("Pontuação Final: "+str(pontos), white, 30, 70, 80)
            pygame.draw.rect(background, white, [45, 120, 135, 27])
            texto("Continuar", black, 30, 50, 125)
            pygame.draw.rect(background, white, [190, 120, 75, 27])
            texto('Sair', black, 30, 195, 125 )
            pygame.display.update()

        # Captura de teclas dentro do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = False # Sai do while
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x =- tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x =+ tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_y =- tamanho
                    velocidade_x = 0
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_y =+ tamanho
                    velocidade_x = 0
                if event.key == pygame.K_ESCAPE:
                    fimdejogo = True

        #Background/Retângulo/FPS/Update/Posição+Velocidade
        if exit:
            background.fill(black)
            pos_x += velocidade_x
            pos_y += velocidade_y

            # Comer maçã
            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura - tamanho, 10)  # 0 até 630
                maca_y = randrange(0, altura - tamanho - 40, 10)
                CobraComp += 1
                pontos += 1

            # Bordas
            if pos_x + tamanho > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x = largura-tamanho
            if pos_y + tamanho > altura-40:
                pos_y = 0
            if pos_y < 0:
                pos_y = altura-tamanho-40

            # Cobra
            CobraInicio = []
            CobraInicio.append(pos_x)
            CobraInicio.append(pos_y)
            CobraXY.append(CobraInicio)
            if len(CobraXY) > CobraComp:
                del CobraXY[0]
            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                fimdejogo = True

            # Pontuação
            pygame.draw.rect(background, white, [0, altura-40, largura, 40])
            texto("Pontuação: "+str(pontos), black, 20, 10, altura-30)

            cobra(CobraXY)
            maca(maca_x, maca_y)

            relogio.tick(15)
            pygame.display.update()

jogo()
pygame.quit()
