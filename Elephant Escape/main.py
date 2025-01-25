import pygame as pg
from sys import exit , executable , argv
from random import randint
from os import execl
from pathlib import Path

from Python.ground import TRACK
from Python.cactus import CACTUS
from Python.dino import DINO
from Python.clouds import CLOUD
from Python.score import SCORE
from Python.reset import GAMEOVER
from Python.start import START
from Python.Bird import BIRD
from Python.funfact import FACT

def restart_program():
    execl(executable, executable, *argv)


data_path = Path("./Data/data.txt")
if data_path.exists():
    with open("./Data/data.txt", "r") as f:
        try:
            highscore = int(f.read().strip())
        except ValueError:
            highscore = 0
else:
    with open("./Data/data.txt", "w") as f:
        f.write("0")
        highscore = 0

pg.init()

SCREEN_WIDTH = 900 
SCREEN_HEIGHT = 600
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.HWSURFACE | pg.DOUBLEBUF) # found this on the internet
pg.display.set_caption("Save The Elephant")

FPS = 90
clock = pg.time.Clock()
dead = False

WHITE = (255,255,255)
DUSK = (71,112,165)
DAWN = (242,242,184)

cacti = []
clouds = [CLOUD(),CLOUD(),CLOUD(),CLOUD(),CLOUD(),CLOUD()]
birds = []

Ground = TRACK()
Cactus = CACTUS()
Dino = DINO()
Score = SCORE()
GameOver = GAMEOVER()
Start = START()
Fact = FACT()

random_spawn_frame = randint(50,60)
cactus_spawn_frame = 0
cactus_spawn_delay = 0

random_spawn_frame_bird = randint(400,600)
bird_spawn_frame = 0
bird_spawn_delay = 0
speed = 1
reset = False

fun_facts = [
    "Poaching disrupts elephant ecosystems",
    "Elephants spread seeds that grow forests",
    "Ivory trade leads to elephant declines",
    "Forest elephants are critical for biodiversity",
    "Poaching weakens entire animal populations",
    "Elephants create waterholes for other species",
    "Ivory bans help reduce illegal poaching",
    "Elephant loss harms ecosystems globally",
    "Protecting elephants supports many species",
    "Anti-poaching laws save keystone species"
]

facts_index = 0

step = 1
number_of_steps = 3000
running = False
end = False

class FAMILY:
    def __init__ (self):
        self.x = 1000
        self.y = 380
        self.width = 600
        self.height = 150
        self.sprite = pg.image.load("./Assets/Other/Family.png").convert_alpha()
        self.sprite = pg.transform.scale(self.sprite, (self.width,self.height))
    def draw(self,scr):
        scr.blit(self.sprite, (self.x,self.y))
    def move(self):
        if self.x > 300: 
            self.x -= 10 
        else:
            self.x = 300  
Family = FAMILY()

while not running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    
    keys = pg.key.get_pressed()
    if any(keys): 
        running = True

    screen.fill(DUSK)
    Ground.draw(screen)
    Dino.draw(screen)
    Start.display(screen) 

    pg.display.flip()      
    clock.tick(FPS) 

while running:
    if not end:
        if Score.score > number_of_steps:
            end = True

    if not end:
        if Score.score <= 3250:
            speed += 0.0003
    delta_time = min(clock.tick(FPS) / 1000,0.1)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:  
            running = False
    

    step += 1

    if step < number_of_steps:
        current_color = [x + (((y-x)/number_of_steps)*step) 
                        for x,y in zip(pg.color.Color(DUSK),
                                            pg.color.Color(DAWN))]
    else:
        current_color = DAWN
    screen.fill(current_color)

    if end:
        Family.draw(screen)
        Family.move()
        Score.score = "Protect our Elephants!"


    if not dead and not end:
        Ground.move(delta_time,speed)
    Ground.draw(screen)

    for cactus in cacti:
        if not dead and not end:
            cactus.move(delta_time,speed)
            cactus.draw(screen)

    cacti = [
        cactus for cactus in cacti if cactus.x >= -50
    ] # Only Cactus that has a higher x than -50 will be rendered
    
    cactus_spawn_delay += 1
    cactus_spawn_frame += 1
    if not dead:
        if (cactus_spawn_frame >= random_spawn_frame and
            bird_spawn_delay > 15):
            random_spawn_frame = randint(40,60)
            cactus_spawn_delay = 0
            cactus_spawn_frame = 0
            Cactus = CACTUS()
            cacti.append(Cactus)

    for bird in birds:
        if not dead:
            bird.move(delta_time,speed)
            bird.animate()
        bird.draw(screen)
    
    birds = [
        bird for bird in birds if bird.x >= -50
    ] # Only Birds that has a higher x than -50 will be rendered
    
    bird_spawn_frame += 1
    bird_spawn_delay += 1
    if not dead and not end:
        if (bird_spawn_frame >= random_spawn_frame_bird and 
        cactus_spawn_delay > 20):
            random_spawn_frame_bird = randint(150,300)
            bird_spawn_frame = 0
            bird_spawn_delay = 0 
            Bird = BIRD()
            birds.append(Bird)

    for cloud in clouds:
        cloud.draw(screen)
        if not dead and not end:
            cloud.move(delta_time,speed)
    
    
    Dino.draw(screen)
    if not end:
        Dino.physics(delta_time)
        Dino.animate()
        collided = Dino.collide(cacti,birds)
        if collided:
            with open("./Data/data.txt", "w") as f:
                f.write(str(highscore))
            Dino.dead = True
            dead = True
    else:
        Dino.y = 430
        Dino.sprite = Dino.dino_sprite_jump

    if not end:
        pass
    if not dead:
        if not end:
            Score.increase(1)
    highscore = Score.display(screen, highscore)

    if not end:
        if Score.score >= 301:
            if not end:
                Fact.display(screen,fun_facts,facts_index)
            if Score.score % 300 == 0:
                facts_index += 1
                if facts_index == len(fun_facts):
                    facts_index = 0

    if dead:
        GameOver.draw(screen,highscore)
        reset = GameOver.check_reset(events)

    if reset:
        with open("./Data/data.txt", "w") as f:
            f.write(str(highscore))
        print("Restarting")
        restart_program()
    
    pg.display.flip()      
    clock.tick(FPS) 

with open("./Data/data.txt", "w") as f:
    f.write(str(highscore))

pg.quit()
exit()