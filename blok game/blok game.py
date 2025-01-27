import random
import itertools
import pgzrun
HEIGHT=400
WIDTH=400
# setting the block positions
listy=[(380,20),(380,380),(20,380),(20,20)]
listie=itertools.cycle(listy)
block=Actor("block.png")
block.pos=(20,20)
def draw():
    screen.clear()
    block.draw()
def bounce():
    animate(block,"bounce_end",duration=0.5,pos=next((listie)))
bounce()
clock.schedule_interval(bounce,2)






pgzrun.go()
