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

FPS = 85
clock = pg.time.Clock()
dead = False

WHITE = (255,255,255) 

cacti = []
clouds = [CLOUD(),CLOUD(),CLOUD(),CLOUD(),CLOUD(),CLOUD()]
birds = []

Ground = TRACK()
Cactus = CACTUS()
Dino = DINO()
Score = SCORE()
GameOver = GAMEOVER()
Start = START()

random_spawn_frame = randint(50,60)
cactus_spawn_frame = 0

random_spawn_frame_bird = randint(400,600)
bird_spawn_frame = 0
speed = 1
reset = False


running = False

while not running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:  
            pg.quit()
            exit()
    
    keys = pg.key.get_pressed()
    if any(keys): 
        running = True

    screen.fill(WHITE)
    Ground.draw(screen)
    Dino.draw(screen)
    Start.display(screen)

    pg.display.flip()      
    clock.tick(FPS) 

while running:
    if Score.score <= 3250:
        speed += 0.0003
    delta_time = min(clock.tick(FPS) / 1000,0.1)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:  
            running = False
    screen.fill(WHITE)
    if not dead:
        Ground.move(delta_time,speed)
    Ground.draw(screen)

    for cactus in cacti:
        if not dead:
            cactus.move(delta_time,speed)
        cactus.draw(screen)

    cacti = [
        cactus for cactus in cacti if cactus.x >= -50
    ] # Only Cactus that has a higher x than -50 will be rendered
    
    cactus_spawn_frame += 1
    if not dead:
        if cactus_spawn_frame >= random_spawn_frame:
            random_spawn_frame = randint(40,60)
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
    if not dead:
        if bird_spawn_frame >= random_spawn_frame_bird:
            random_spawn_frame_bird = randint(300,600)
            bird_spawn_frame = 0
            Bird = BIRD()
            birds.append(Bird)

    for cloud in clouds:
        cloud.draw(screen)
        if not dead:
            cloud.move(delta_time,speed)
    
    Dino.draw(screen)
    Dino.physics(delta_time)
    Dino.animate()
    collided = Dino.collide(cacti,birds)
    if collided:
        with open("./Data/data.txt", "w") as f:
            f.write(str(highscore))
        Dino.dead = True
        dead = True

    if not dead:
        Score.increase(1)
    highscore = Score.display(screen, highscore)

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