import pygame
import random
from classe_blocos import Bloco
from classe_jogador import jogador
pygame.init()
#Dimensões-----------------------------------------------------------------------------------
width = 800
height = 800
#Background----------------------------------------------------------------------------------
background = pygame.image.load('stars.png')
background = pygame.transform.scale(background, (width,height))
background_inicial = pygame.image.load('startbackground.png')
background_inicial = pygame.transform.scale(background_inicial,(width,height))
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")
#SOM------------------------------------------------------------------------------------------
brickHitSound = pygame.mixer.Sound("bullet.wav")
bounceSound = pygame.mixer.Sound("hitGameSound.wav")
background_sound = pygame.mixer.Sound('background_music.wav')
bounceSound.set_volume(.2)
#TEXTO_TELA_INICIAL-----------------------------------------------------------------------------------
branco = pygame.Color('grey100')
preto = pygame.Color('grey0')
Inicio_font = pygame.font.Font('Kaph-Italic.ttf', 60)
barra_font = pygame.font.Font('Kaph-Italic.ttf', 10)
ini_txt = Inicio_font.render('Breakout', False, branco)
Barra_txt = Inicio_font.render('Pressione Espaço', False, branco)
Barra2_txt = Inicio_font.render('para começar', False, branco)
#TELA_INICIAL-----------------------------------------------------------------------------------------
Inicial = True
while Inicial:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Inicial = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Inicial = False
    window.fill(branco)
    window.blit(background_inicial,(0,0))
    window.blit(ini_txt, (200, 100 ))
    window.blit(Barra_txt, (30, 500))
    window.blit(Barra2_txt, (90, 600))
    background_sound.play()
    pygame.display.update()

clock = pygame.time.Clock()
FPS = 30
#classe Bola-------------------------------------------------------------------
class Ball(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.xv = random.randint(-6,6)
        self.yv = 6
        self.xx = self.x + self.w
        self.yy = self.y + self.h

    def draw(self, win):
        pygame.draw.circle(win, self.color, [self.x, self.y],12,6)

    def move(self):
        self.x += self.xv
        self.y += self.yv
#Funções ---------------------------------------------------------------------
bricks = []
def init():
    global bricks
    bricks = []
    for i in range(6):
        for j in range(10):
            cor_bloco = random.choice(cores)
            bricks.append(Bloco(10 + j * 79, 50 + i * 35, 70, 25, cor_bloco))
gameover = False
def redrawGameWindow():
    window.blit(background, (0,0))
    Jogador.draw(window)
    for ball in bolas:
        ball.draw(window)
    for b in bricks:
        b.draw(window)

    fonte = pygame.font.Font('Kaph-Italic.ttf', 25)

    if gameover:
        if len(bricks) == 0:
            resText = fonte.render("Parabéns!", 1, (255, 255, 255))
        else:
            resText = fonte.render("Perdeu!", 1, (255, 255, 255))
        window.blit(resText, ((width//2 - resText.get_width()//2), height//2 - resText.get_height()//2))
        playAgainText = fonte.render("Aperte Espaço para jogar de novo", 1, (255, 255, 255))
        window.blit(playAgainText, ((width//2 - playAgainText.get_width()//2), height//2 + 30 ))

    pygame.display.update()
#Cores------------------------------------------------------------------------
azul = pygame.Color('blue')
rosa = pygame.Color('deeppink')
laranja = pygame.Color('firebrick1')
amarelo = pygame.Color('gold')
verde = pygame.Color('green')
cores = [azul,laranja,rosa,amarelo,verde,branco]
cor_jog = random.choice(cores)
cor_bola = random.choice(cores)
cor_bloco = random.choice(cores)
#CHAMANDO AS CLASSES----------------------------------------------------------
Jogador = jogador(width/2 - 50,height-100,140,20,cor_jog)
bola = Ball(width/2 - 10, height - 400, 20, 20, cor_bola)
bolas = [bola]
init()
#Loop_principal--------------------------------------------------------------
game = True
background_sound.stop()
while game and Inicial==False:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    if not gameover:
        for ball in bolas:
            ball.move()
        if pygame.mouse.get_pos()[0] - Jogador.w//2 < 0:
            Jogador.x = 0
        elif pygame.mouse.get_pos()[0] + Jogador.w//2 > width:
            Jogador.x = width - Jogador.w
        else:
            Jogador.x = pygame.mouse.get_pos()[0] - Jogador.w //2

        for ball in bolas:
            if (ball.x >= Jogador.x and ball.x <= Jogador.x + Jogador.w) or (ball.x + ball.w >= Jogador.x and ball.x + ball.w <= Jogador.x + Jogador.w):
                if ball.y + ball.h >= Jogador.y and ball.y + ball.h <= Jogador.y + Jogador.h:
                    ball.yv *= -1
                    ball.y = Jogador.y -ball.h -1
                    bounceSound.play()

            if ball.x + ball.w >= width:
                bounceSound.play()
                ball.xv *= -1
            if ball.x < 0:
                bounceSound.play()
                ball.xv *= -1
            if ball.y <= 0:
                bounceSound.play()
                ball.yv *= -1

            if ball.y > height:
                bolas.pop(bolas.index(ball))

        for brick in bricks:
            for ball in bolas:
                if (ball.x >= brick.x and ball.x <= brick.x + brick.w) or ball.x + ball.w >= brick.x and ball.x + ball.w <= brick.x + brick.w:
                    if (ball.y >= brick.y and ball.y <= brick.y + brick.h) or ball.y + ball.h >= brick.y and ball.y + ball.h <= brick.y + brick.h:
                        brick.visible = False
                        if brick.pregnant:
                            cor_bola = random.choice(cores)
                            bolas.append(Ball(brick.x, brick.y, 20, 20, cor_bola))
                        #bricks.pop(bricks.index(brick))
                        ball.yv *= -1
                        brickHitSound.play()
                        break

        for brick in bricks:
            if brick.visible == False:
                bricks.pop(bricks.index(brick))

        if len(bolas) == 0:
            gameover = True


    keys = pygame.key.get_pressed()
    if len(bricks) == 0:
        won = True
        gameover = True
    if gameover:
        if keys[pygame.K_SPACE]:
            gameover = False
            won = False
            cor_bola = random.choice(cores)
            bola = Ball(width/2 - 10, height - 400, 20, 20, cor_bola)
            bolas = [bola]
            if len(bolas) == 0:
                bolas.append(bola)

            bricks.clear()
            for i in range(6):
                for j in range(10):
                    cor_bloco = random.choice(cores)
                    bricks.append(Bloco(10 + j * 79, 50 + i * 35, 70, 25, cor_bloco))
    redrawGameWindow()
    window.fill(branco)
    window.blit(background, (0,0))

#Texto final--------------------------------------------------
final_txt = Inicio_font.render('Bom Jogo!', False, branco)
final1_txt = Inicio_font.render('Volte novamente!', False, branco)
final2_txt = Inicio_font.render('Até mais!', False, branco)
#Tela Final----------------------------------
final = True
background_sound.play()
while final:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            final = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                final = False
    window.fill(branco)
    window.blit(background_inicial,(0,0))
    window.blit(final_txt, (200, 100 ))
    window.blit(final1_txt, (30, 500))
    window.blit(final2_txt, (90, 600))
    pygame.display.update()