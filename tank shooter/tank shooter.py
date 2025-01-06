import pgzrun
import random
WIDTH=1200
HEIGHT=600
# definding colors
blu=(0,0,255)
Listb=[]
#actor
tank=Actor("tank.png")
bug=Actor("bug.png")
bug.y=0
bug.x=random.randint(0,1200)
tank.pos=600,530
def draw():
    screen.blit("field.jpg",(0,0))
    bug.draw()
    tank.draw()
    for i in Listb:
        i.draw()
def on_key_down(key):
    if key==keys.SPACE:
        Listb.append(Actor("tank bullet.png"))
        Listb[-1].x=tank.x
        Listb[-1].y=tank.y-50
def update():
    pass
    if keyboard.left:
        tank.x-=10
    if keyboard.right:
        tank.x+=10
    for i in Listb:
        i.y-=50
    bug.y+=3
    if bug.y==600:
        bug.y=0
        bug.x=random.randint(0,1200)

pgzrun.go()
