import pgzrun
import random
WIDTH=1200
HEIGHT=600
# definding colors
blu=(0,0,255)
#actor
tank=Actor("tank.png")
tank.pos=600,530
def draw():
    screen.blit("field.jpg",(0,0))
    tank.draw()
def update():
    pass
    if keyboard.left:
        tank.x-=10
    if keyboard.right:
        tank.x+=10

pgzrun.go()