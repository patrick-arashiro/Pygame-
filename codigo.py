import pygame
import random
pygame.init()

width = 800
height = 800

background = pygame.image.load('stars.png')
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")
#Planetas----------------------------------------------------------------------------------
width_planets = 25
height_planets = 25
terra_img = pygame.image.load('Terran.png').convert_alpha()
terra_img = pygame.transform.scale(terra_img, (width_planets, height_planets))
lava_img = pygame.image.load('Lava.png').convert_alpha()
lava_img = pygame.transform.scale(lava_img,(width_planets, height_planets))
Ice_img = pygame.image.load('Ice.png')
Ice_img = pygame.transform.scale(Ice_img, (width_planets, height_planets))
black_hole_img = pygame.image.load('Black_hole.png').convert_alpha()
black_hole_img = pygame.transform.scale(black_hole_img, (width_planets, height_planets))
baren_img = pygame.image.load('Baren.png')
baren_img = pygame.transform.scale(baren_img, (width_planets, height_planets))
#SOM------------------------------------------------------------------------------------------
brickHitSound = pygame.mixer.Sound("bullet.wav")
bounceSound = pygame.mixer.Sound("hitGameSound.wav")
bounceSound.set_volume(.2)
#TEXTO_TELA_INICIAL-----------------------------------------------------------------------------------
branco = pygame.Color('grey100')
preto = pygame.Color('grey0')
Inicio_font = pygame.font.Font('Kaph-Italic.ttf', 60)
barra_font = pygame.font.Font('Kaph-Italic.ttf', 10)
ini_txt = Inicio_font.render('Breakout', False, preto)
Barra_txt = Inicio_font.render('Pressione Espaço', False, preto)
Barra2_txt = Inicio_font.render('para começar', False, preto)
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
    window.blit(ini_txt, (200, 100 ))
    window.blit(Barra_txt, (30, 500))
    window.blit(Barra2_txt, (90, 600))
    pygame.display.update()
clock = pygame.time.Clock()

gameover = False
