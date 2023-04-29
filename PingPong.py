from pygame import *
from random import *
from time import time as timer


window = display.set_mode((700,500))
display.set_caption('Пинг-понг') 
background = (0,180,255)
window.fill(background)


clock = time.Clock()
FPS = 60

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False










    clock.tick(FPS)
    display.update()