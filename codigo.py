import pygame
import random
pygame.init()

weight = 800
height = 800

background = pygame.image.load('stars.png')
window = pygame.display.set_mode((weight, height))
pygame.display.set_caption("Breakout")
#Planetas-----------------------------------------
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

brickHitSound = pygame.mixer.Sound("bullet.wav")
bounceSound = pygame.mixer.Sound("hitGameSound.wav")
bounceSound.set_volume(.2)

clock = pygame.time.Clock()

gameover = False
