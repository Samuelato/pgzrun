import random
import itertools
import pgzrun
HEIGHT=400
WIDHT=400
# setting the block positions
listy=[(20,20),(380,20),(380,380),(20,380)]
listie=itertools.cycle(listy)
block=Actor("block.png")
block.pos=(20,20)
def draw():
    block.draw()








pgzrun.go()