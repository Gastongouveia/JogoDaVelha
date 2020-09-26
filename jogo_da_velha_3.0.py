import pygame
from sys import exit
from time import sleep
import socket

#função que desenha o tabuleiro na tela
def desenhar_tab():
    img_tabuleiro = pygame.image.load("tabuleiro.png")
    tela.blit(img_tabuleiro,(0,0))

#função que desenha o "x" ou "y" no tabuleiro
def marcar_tab(posição):
    x, y = posição
    if jogador == 1:
        img_x = pygame.image.load("x.png")
        tela.blit(img_x,[(x + 20), (y + 20)])
    if jogador == 2:
        img_o = pygame.image.load("o.png")
        tela.blit(img_o,[(x + 20), (y + 20)])

#função que identifica a posição onde o "x" ou "y" será desenhado
def marcar_posição():
    global servidor
    if servidor == "s":
        for p in quadrados:
            if evento.type == pygame.MOUSEBUTTONDOWN and p.collidepoint(posição_mouse):
                if p == quadrado0:
                    teste_posição(0, 0,(0, 0))
                    sock.sendto(bytes([0, 0, 0, 0]), address)
                elif p == quadrado1:
                    teste_posição(0, 1, (200, 0))
                    sock.sendto(bytes([0, 1, 200, 0]), address)
                elif p == quadrado2:
                    teste_posição(0, 2, (400, 0))
                    sock.sendto(bytes([0, 2, 4, 0]), address)
                elif p == quadrado3:
                    teste_posição(1, 0, (0, 200))
                    sock.sendto(bytes([1, 0, 0, 200]), address)
                elif p == quadrado4:
                    teste_posição(1, 1, (200, 200))
                    sock.sendto(bytes([1, 1, 200, 200]), address)
                elif p == quadrado5:
                    teste_posição(1, 2, (400, 200))
                    sock.sendto(bytes([1, 2, 4, 200]), address)
                elif p == quadrado6:
                    teste_posição(2, 0, (0, 400))
                    sock.sendto(bytes([2, 0, 0, 4]), address)
                elif p == quadrado7:
                    teste_posição(2, 1, (200, 400))
                    sock.sendto(bytes([2, 1, 200, 4]), address)
                elif p == quadrado8:
                    teste_posição(2, 2, (400, 400))
                    sock.sendto(bytes([2, 2, 4, 4]), address)
    else:
        for p in quadrados:
            if evento.type == pygame.MOUSEBUTTONDOWN and p.collidepoint(posição_mouse):
                if p == quadrado0:
                    teste_posição(0, 0,(0, 0))
                    sock.sendto(bytes([0, 0, 0, 0]), server_address)
                elif p == quadrado1:
                    teste_posição(0, 1, (200, 0))
                    sock.sendto(bytes([0, 1, 200, 0]), server_address)
                elif p == quadrado2:
                    teste_posição(0, 2, (400, 0))
                    sock.sendto(bytes([0, 2, 4, 0]), server_address)
                elif p == quadrado3:
                    teste_posição(1, 0, (0, 200))
                    sock.sendto(bytes([1, 0, 0, 200]), server_address)
                elif p == quadrado4:
                    teste_posição(1, 1, (200, 200))
                    sock.sendto(bytes([1, 1, 200, 200]), server_address)
                elif p == quadrado5:
                    teste_posição(1, 2, (400, 200))
                    sock.sendto(bytes([1, 2, 4, 200]), server_address)
                elif p == quadrado6:
                    teste_posição(2, 0, (0, 400))
                    sock.sendto(bytes([2, 0, 0, 4]), server_address)
                elif p == quadrado7:
                    teste_posição(2, 1, (200, 400))
                    sock.sendto(bytes([2, 1, 200, 4]), server_address)
                elif p == quadrado8:
                    teste_posição(2, 2, (400, 400))
                    sock.sendto(bytes([2, 2, 4, 4]), server_address)
        


#função que verifica se a posição já foi escolhida
def teste_posição(linha, coluna, posição):
    global simbolo, jogador, estado, jogadas
    if matriz_tabuleiro[linha][coluna] == "x" or matriz_tabuleiro[linha][coluna] == "o":
        print("posição já foi escolhida")
    else:
        matriz_tabuleiro[linha][coluna] = simbolo
        marcar_tab(posição)
        teste_vitoria(linha, coluna, simbolo)
        print(matriz_tabuleiro)
        jogadas += 1
        if estado == "ativo":
            if jogador == 1:
                jogador = 2
                simbolo = "o"
            else:
                jogador = 1
                simbolo = "x"

def teste_vitoria(linha, coluna, s):
    global jogador, estado
    if ((matriz_tabuleiro[linha][0] == s and matriz_tabuleiro[linha][1] == s and matriz_tabuleiro[linha][2] == s) or 
    (matriz_tabuleiro[0][coluna] == s and matriz_tabuleiro[1][coluna] == s and matriz_tabuleiro[2][coluna] == s) or 
    (matriz_tabuleiro[0][0] == s and matriz_tabuleiro[1][1] == s and matriz_tabuleiro[2][2] == s) or 
    (matriz_tabuleiro[2][0] == s and matriz_tabuleiro[1][1] == s and matriz_tabuleiro[0][2] == s)):
        print(f"jodador {jogador} venceu")
        estado = "final"

def reset():
    global matriz_tabuleiro, jogador, simbolo, estado, jogadas

    tela.fill(branco)

    desenhar_tab()
    matriz_tabuleiro = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    jogador = 1
    simbolo = "x"
    estado = "ativo"
    jogadas = 0
            

#Cores no padrão RGB
rosa = (201, 30, 151)
azul = (0, 0, 255)
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255,0,0)

servidor = input("Este é o servidor? \n(s) Sim \n(n) Não : ")

if servidor == "s":

    pygame.init()

    tela = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Jogo da velha - Servidor - Jogador 1')
    tela.fill(branco)
    fonte = pygame.font.SysFont("Comic Sans MS", 70)
    pygame.mixer.music.load("SuTurno.ogg")
    pygame.mixer.music.play(-1)

    matriz_tabuleiro = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    #delimitando os quadrados do tabuleiro
    quadrado0 = pygame.Rect((0, 0), (200, 200),)
    quadrado1 = pygame.Rect((200, 0), (200, 200))
    quadrado2 = pygame.Rect((400, 0), (200, 200))
    quadrado3 = pygame.Rect((0, 200), (200, 200))
    quadrado4 = pygame.Rect((200, 200), (200, 200))
    quadrado5 = pygame.Rect((400, 200), (200, 200))
    quadrado6 = pygame.Rect((0, 400), (200 ,200))
    quadrado7 = pygame.Rect((200, 400), (200 ,200))
    quadrado8 = pygame.Rect((400, 400), (200, 200))
    quadrados = [quadrado0, quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8]

    jogador = 1
    simbolo = "x"
    estado = "ativo"
    jogadas = 0
    vitoria_j1 = 0
    vitoria_j2 = 0

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 10000)

    sock.bind(server_address)
    print("\nEsperando a mensagem")
    data, address = sock.recvfrom(1024)

    while True:

        desenhar_tab()

        if jogador == 2:
            data, address = sock.recvfrom(1024)
            argumentos = data
            linha = int(argumentos[0])
            coluna = int(argumentos[1])
            posição_x = int(argumentos[2])
            if posição_x == 4:
                posição_x = 400
            posição_y = int(argumentos[3])
            if posição_y == 4:
                posição_y = 400
            posição = (posição_x, posição_y)
            teste_posição(linha, coluna, posição)

        else:
            posição_mouse = pygame.mouse.get_pos()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sock.close()
                    exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    marcar_posição()
        
        pygame.display.flip()
        if estado == "final":
            if jogador == 1:
                vitoria_j1 += 1
                pygame.display.flip()
                sleep(0.5)
                tela.fill(branco)
                img_vitoria_j1 = pygame.image.load("vitoria_j1.png")
                tela.blit(img_vitoria_j1,(0,0))
                texto1 = fonte.render(f"{vitoria_j1}", True, rosa)
                texto2 = fonte.render(f"{vitoria_j2}", True, rosa)
                tela.blit(texto1, [210, 465])
                tela.blit(texto2, [350, 465])
                pygame.display.flip()
                sleep(5)
                reset()
            else:
                vitoria_j2 += 1
                pygame.display.flip()
                sleep(0.5)
                tela.fill(branco)
                img_vitoria_j2 = pygame.image.load("vitoria_j2.png")
                tela.blit(img_vitoria_j2,(0,0))
                texto1 = fonte.render(f"{vitoria_j1}", True, rosa)
                texto2 = fonte.render(f"{vitoria_j2}", True, rosa)
                tela.blit(texto1, [210, 465])
                tela.blit(texto2, [350, 465])
                pygame.display.flip()
                sleep(5)
                reset()
        else:
            if jogadas == 9:
                pygame.display.flip()
                sleep(2)
                tela.fill(branco)
                img_empate = pygame.image.load("empate.png")
                tela.blit(img_empate,(0,0))
                pygame.display.flip()
                sleep(5)
                reset()

elif servidor == "n":
    pygame.init()

    tela = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Jogo da velha - Cliente - Jogador 2')
    tela.fill(branco)
    fonte = pygame.font.SysFont("Comic Sans MS", 70)
    pygame.mixer.music.load("SuTurno.ogg")
    pygame.mixer.music.play(-1)

    matriz_tabuleiro = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    #delimitando os quadrados do tabuleiro
    quadrado0 = pygame.Rect((0, 0), (200, 200),)
    quadrado1 = pygame.Rect((200, 0), (200, 200))
    quadrado2 = pygame.Rect((400, 0), (200, 200))
    quadrado3 = pygame.Rect((0, 200), (200, 200))
    quadrado4 = pygame.Rect((200, 200), (200, 200))
    quadrado5 = pygame.Rect((400, 200), (200, 200))
    quadrado6 = pygame.Rect((0, 400), (200 ,200))
    quadrado7 = pygame.Rect((200, 400), (200 ,200))
    quadrado8 = pygame.Rect((400, 400), (200, 200))
    quadrados = [quadrado0, quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8]

    jogador = 1
    simbolo = "x"
    estado = "ativo"
    jogadas = 0
    vitoria_j1 = 0
    vitoria_j2 = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    sent = sock.sendto(bytes("conectando", "utf-8"), server_address)

    while True:
        
        desenhar_tab()
        pygame.display.flip()
        
        if jogador == 1:
            data, server = sock.recvfrom(1024)
            argumentos = data
            linha = int(argumentos[0])
            coluna = int(argumentos[1])
            posição_x = int(argumentos[2])
            if posição_x == 4:
                posição_x = 400
            posição_y = int(argumentos[3])
            if posição_y == 4:
                posição_y = 400
            posição = (posição_x, posição_y)
            teste_posição(linha, coluna, posição)
        
        else:
            posição_mouse = pygame.mouse.get_pos()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sock.close()
                    exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    marcar_posição()
            
            pygame.display.flip()
        if estado == "final":
            if jogador == 1:
                vitoria_j1 += 1
                pygame.display.flip()
                sleep(0.5)
                tela.fill(branco)
                img_vitoria_j1 = pygame.image.load("vitoria_j1.png")
                tela.blit(img_vitoria_j1,(0,0))
                texto1 = fonte.render(f"{vitoria_j1}", True, rosa)
                texto2 = fonte.render(f"{vitoria_j2}", True, rosa)
                tela.blit(texto1, [210, 465])
                tela.blit(texto2, [350, 465])
                pygame.display.flip()
                sleep(5)
                reset()
            else:
                vitoria_j2 += 1
                pygame.display.flip()
                sleep(0.5)
                tela.fill(branco)
                img_vitoria_j2 = pygame.image.load("vitoria_j2.png")
                tela.blit(img_vitoria_j2,(0,0))
                texto1 = fonte.render(f"{vitoria_j1}", True, rosa)
                texto2 = fonte.render(f"{vitoria_j2}", True, rosa)
                tela.blit(texto1, [210, 465])
                tela.blit(texto2, [350, 465])
                pygame.display.flip()
                sleep(5)
                reset()
        else:
            if jogadas == 9:
                pygame.display.flip()
                sleep(2)
                tela.fill(branco)
                img_empate = pygame.image.load("empate.png")
                tela.blit(img_empate,(0,0))
                pygame.display.flip()
                sleep(5)
                reset()
else:
    print("Opção inválida \nEncerrando o programa...")
    sleep(2)
    exit()