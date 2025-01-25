import pygame as pg

class GAMEOVER:
    def __init__(self):
        self.GameOver = pg.image.load("./Assets/Other/GameOver.png").convert_alpha()
        self.Reset = pg.image.load("./Assets/Other/Reset.png").convert_alpha()
        self.ResetRect = self.Reset.get_rect(topleft=(420, 330))  # Match the position where the reset button is drawn
        self.font_size = 40
        self.font = pg.font.Font("./Assets/fonts/PixelFont.ttf", self.font_size) 
        self.color = (0, 0, 0)
    def draw(self, scr , highscore):
        scr.blit(self.GameOver, (270, 250))
        scr.blit(self.Reset, self.ResetRect.topleft)
        score_text = self.font.render(f"HighScore: {highscore}", True, self.color) 
        scr.blit(score_text, (270, 450)) 
        

    def check_reset(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                if self.ResetRect.collidepoint(mouse_pos):
                    return True
        return False