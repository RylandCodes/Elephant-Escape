import pygame as pg



class TRACK:
     def __init__ (self):
          GROUND_SPRITE = pg.image.load("./Assets/Other/Track.png").convert_alpha()
          self.x1 = 0
          self.x2 = 900
          self.y = 420
          self.width = 900
          self.height = 200
          self.sprite = GROUND_SPRITE

          self.sprite = pg.transform.scale(self.sprite, (self.width,self.height))
     def draw(self,scr):
         scr.blit(self.sprite, (self.x1,self.y)) # Ground 1
         scr.blit(self.sprite, (self.x2,self.y)) # Ground 2

     def move(self,delta,speed):
        self.x1 -= (1600 * delta) * speed
        self.x2 -= (1600 * delta) * speed
        if self.x1 <= -self.width:
            self.x1 = self.x2 + self.width
        if self.x2 <= -self.width:
            self.x2 = self.x1 + self.width
     
     