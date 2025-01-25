import pygame as pg

class START:
    def __init__(self):
        self.x = 160
        self.y = 250
        self.font_size = 60
        self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
        self.color = (0, 0, 0)
    
    
    def display(self, screen):
        score_text = self.font.render(f"Press any key to start", True, self.color) 
        screen.blit(score_text, (self.x, self.y)) 