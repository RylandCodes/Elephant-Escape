import pygame as pg



class DINO:
    def __init__(self):
        self.dino_sprite_run1 = pg.image.load("./Assets/Dino/DinoRun1.png").convert_alpha()
        self.dino_sprite_run2 = pg.image.load("./Assets/Dino/DinoRun2.png").convert_alpha()
        self.dino_sprite_jump = pg.image.load("./Assets/Dino/DinoJump.png").convert_alpha()
        self.dino_sprite_duck1 = pg.image.load("./Assets/Dino/DinoDuck1.png").convert_alpha()
        self.dino_sprite_duck2 = pg.image.load("./Assets/Dino/DinoDuck2.png").convert_alpha()
        self.dino_sprite_dead = pg.image.load("./Assets/Dino/DinoDead.png").convert_alpha()
        self.width = 100
        self.height = 100
        self.sprite = self.dino_sprite_jump
        self.sprite = pg.transform.scale(self.sprite,(self.width,self.height))
        self.x = 50
        self.y = 430
        self.mask = pg.mask.from_surface(self.sprite)
        self.velocity = 0
        self.fall_speed = 300
        self.jump_power = -1710
        self.on_ground = True
        self.run_frame = 0
        self.duck_frame = 0
        self.duck = False
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.physictick = 0 # every 3 ticks update physics
        self.dead = False

    def draw(self, screen):
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.sprite = pg.transform.scale(self.sprite, (self.width, self.height))
        screen.blit(self.sprite, (self.x, self.y))
        self.rect.topleft = (self.x, self.y) 
        self.mask = pg.mask.from_surface(self.sprite)

    def physics(self,delta):
        if not self.dead:
            self.physictick += 1
            if self.physictick >= 2:
                self.physictick = 0
                if self.y < 430:  
                    self.velocity += self.fall_speed
                    self.on_ground = False
                else: 
                    self.y = 430
                    self.velocity = 0
                    self.on_ground = True

                keys = pg.key.get_pressed()
                if (keys[pg.K_w] or keys[pg.K_SPACE] or keys[pg.K_UP]) and self.on_ground: 
                    self.velocity = self.jump_power
                    self.on_ground = False


                if self.on_ground:
                    if (keys[pg.K_s] or keys[pg.K_DOWN]):
                        self.duck = True
                        self.height = 70
                        self.y = 460
                    else:
                        self.duck = False
                        self.height = 100
                        self.y = 430
            self.y += self.velocity * delta

            if not self.duck and self.y >= 430:
                self.y = 430
    

    def animate(self):
        if not self.dead:
            if self.on_ground: 
                if self.duck:
                    self.duck_frame += 1
                    if self.duck_frame < 3:
                        self.sprite = self.dino_sprite_duck1
                    elif self.duck_frame < 6:
                        self.sprite = self.dino_sprite_duck2
                    else:
                        self.duck_frame = 0
                else:
                    self.run_frame += 1
                    if self.run_frame < 3:
                        self.sprite = self.dino_sprite_run1
                    elif self.run_frame < 6:
                        self.sprite = self.dino_sprite_run2
                    else:
                        self.run_frame = 0
            else:
                self.sprite = self.dino_sprite_jump
                self.run_frame = 0
                self.duck = False
                self.height = 100 
        else:
            self.sprite = self.dino_sprite_dead
            self.run_frame = 0
            self.duck_frame = 0
    def collide(self,cacti,birds):
        for cactus in cacti:
            if cactus.rect.colliderect(self.rect):
                target_offset = (int(self.x - cactus.rect.x), int(self.y - cactus.rect.y))
                if cactus.mask.overlap(self.mask, target_offset):
                    return True
        for bird in birds:
            if bird.rect.colliderect(self.rect):
                target_offset = (int(self.x - bird.rect.x), int(self.y - bird.rect.y))
                if bird.mask.overlap(self.mask, target_offset):
                    return True
        return False
                

        

    