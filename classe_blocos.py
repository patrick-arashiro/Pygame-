import pygame,random

class Bloco(object):
    def _init_(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.visible = True
        self.xx = self.x + self.w
        self.yy = self.y + self.h

        self.ranNum = random.randint(0,10)
        if self.ranNum < 3:
            self.pregnant = True
        else:
            self.pregnant = False


    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])
