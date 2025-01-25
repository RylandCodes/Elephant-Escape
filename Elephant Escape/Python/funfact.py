import pygame as pg

class FACT:
     def __init__(self):
          self.x = 0
          self.y = 200
          self.font_size = 40
          self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
          self.color = (0, 0, 0)


     def display(self, screen ,facts, index):
          facts_text = self.font.render(f"{facts[index]}", True, self.color)
          self.x = 50
          screen.blit(facts_text, (self.x, self.y)) 

