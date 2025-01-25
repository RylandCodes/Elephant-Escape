import pygame as pg
from random import randint

class CLOUD:
    def __init__(self):
        self.CLOUD_SPRITE = pg.image.load("./Assets/Other/Cloud.png").convert_alpha()
        self.x = randint(1000,7000)
        self.y = randint(50,200)
        self.scale = randint(100,150)
        self.sprite = self.CLOUD_SPRITE
        self.sprite = pg.transform.scale(self.sprite, (self.scale, self.scale))

    def draw(self, scr):
        scr.blit(self.sprite, (self.x, self.y))

    def move(self,delta,speed):
        self.x -= (900 * delta) * speed

        if self.x <= -100:
            self.x = randint(1000,7000)
            self.y = randint(50,200)
            self.scale = randint(100,150)
            self.sprite = self.CLOUD_SPRITE
            self.sprite = pg.transform.scale(self.sprite, (self.scale, self.scale))