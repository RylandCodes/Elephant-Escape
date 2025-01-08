import pygame as pg

class SCORE:
    def __init__(self):
        self.x = 410
        self.y = 20
        self.font_size = 60
        self.score = 0  
        self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
        self.color = (60, 60, 60)
    def increase(self, amount):
        self.score += amount
    
    
    def display(self, screen , highscore):
        score_text = self.font.render(f"{self.score}", True, self.color) 
        screen.blit(score_text, (self.x, self.y)) 
        if self.score >= highscore:
            highscore = self.score
        return highscore