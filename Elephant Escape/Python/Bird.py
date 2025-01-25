import pygame as pg
import random

class BIRD:
    def __init__(self):
        self.BIRD_SPRITES = [
            pg.image.load("./Assets/Bird/Bird1.png").convert_alpha(),
            pg.image.load("./Assets/Bird/Bird2.png").convert_alpha()
        ]
        self.x = 1000
        self.y = 375
        self.width = 125
        self.height = 105
        self.sprite = self.BIRD_SPRITES[0]
        self.sprite = pg.transform.scale(self.sprite, (self.width, self.height))
        self.mask = pg.mask.from_surface(self.sprite)
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.frame = 0
    def draw(self, scr):
        scr.blit(self.sprite, (self.x, self.y))
        self.rect.topleft = (self.x, self.y) 

    def move(self,delta,speed):
        self.x -= (1600 * delta) * speed

    def animate(self):
        self.frame += 1
        if self.frame < 5:
            self.sprite = self.BIRD_SPRITES[0]
        elif self.frame < 10:
            self.sprite = self.BIRD_SPRITES[1]
        else:
            self.frame = 0