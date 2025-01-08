import pygame as pg
import random

class CACTUS:
    def __init__(self):
        CACTUS_SPRITES = [
            pg.image.load("./Assets/Cactus/LargeCactus2.png").convert_alpha(),
            pg.image.load("./Assets/Cactus/LargeCactus3.png").convert_alpha(),
            pg.image.load("./Assets/Cactus/SmallCactus1.png").convert_alpha(),
            pg.image.load("./Assets/Cactus/SmallCactus2.png").convert_alpha(),
            pg.image.load("./Assets/Cactus/SmallCactus3.png").convert_alpha(),
        ]
        self.x = 1000
        self.y = 440
        self.width = 125
        self.height = 105
        self.sprite = random.choice(CACTUS_SPRITES)
        self.sprite = pg.transform.scale(self.sprite, (self.width, self.height))
        self.mask = pg.mask.from_surface(self.sprite)
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))

    def draw(self, scr):
        scr.blit(self.sprite, (self.x, self.y))
        self.rect.topleft = (self.x, self.y) 

    def move(self,delta,speed):
        self.x -= (1600 * delta) * speed