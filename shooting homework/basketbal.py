import pgzrun
import random
TITLE= "shooting a basketball"
WIDTH=400
HEIGHT=400
bask=Actor("bal.png")
def draw():
    screen.clear()
    screen.fill("brown")
    bask.draw()
def bals():
    bask.x=random.randint(0,400)
    bask.y=random.randint(0,400)
def on_mouse_down(pos):
    if bask.collidepoint(pos):
      bals()  

pgzrun.go()