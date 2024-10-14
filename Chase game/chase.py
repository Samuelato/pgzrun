import random
import pgzrun
import time
WIDTH=400
HEIGHT=400
thib=Actor("thib.png")
bal=Actor("bal.png")
def draw():
    thib.draw()
    bal.draw()
pgzrun.go()