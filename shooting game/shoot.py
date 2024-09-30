import pgzrun
import random
TITLE="shooting neymar"
WIDTH=400
HIGTH=400
#actor methoth to create a sprite
ney=Actor("player.png")
def draw():
    ney.draw()
pgzrun.go()