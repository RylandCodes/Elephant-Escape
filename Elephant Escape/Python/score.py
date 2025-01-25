import pygame as pg

class SCORE:
    def __init__(self):
        self.x = 410
        self.y = 20
        self.font_size = 60
        self.score = 0  
        self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
        self.color = (0, 0, 0)
    def increase(self, amount):
        self.score += amount
    
    
    def display(self, screen , highscore):
        if self.score == "Protect our Elephants!":
            self.x = 50
        score_text = self.font.render(f"{self.score}", True, self.color) 
        screen.blit(score_text, (self.x, self.y)) 
        if not self.score == "Protect our Elephants!":
            if self.score >= highscore:
                highscore = self.score
        return highscore