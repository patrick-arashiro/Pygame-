import pygame
import random
pygame.init()

weight = 800
height = 800

bg = pygame.image.load('stars.png')
win = pygame.display.set_mode((weight, height))
pygame.display.set_caption("Breakout")

brickHitSound = pygame.mixer.Sound("bullet.wav")
bounceSound = pygame.mixer.Sound("hitGameSound.wav")
bounceSound.set_volume(.2)

clock = pygame.time.Clock()

gameover = False


print('óla')
print('funciona')
game = False