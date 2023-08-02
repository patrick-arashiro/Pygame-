import random
import pygame

width = 800
height = 800
class Planetas(pygame.sprite.Sprite):
    def _init_(self, img):
        pygame.sprite.Sprite._init_(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (width / 2) - 12.5
        self.rect.y = (height / 2) - 12.5
        self.speedx = 2 * random.choice((1, -1))
        self.speedy = 2 * random.choice((1, -1))
        self.ultima_atualizacao = 0

    def update(self):
        agora = pygame.time.get_ticks()
        if agora - self.ultima_atualizacao >3000:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        if pygame.sprite.collide_rect(self) or pygame.sprite.collide_rect(self):
            self.speedx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speedy *= -1
        if self.rect.right >= width:
            self.rect.x = width/2 - 12.5
            self.rect.y = height/2 -12.5
            self.speedx =  2 * random.choice((1, -1))
            self.ultima_atualizacao = pygame.time.get_ticks()
        if self.rect.left <= 0:
            self.rect.x = width/2 - 12.5
            self.rect.y = height/2- 12.5
            self.speedx =  2 * random.choice((1, -1))
            self.ultima_atualizacao = pygame.time.get_ticks()