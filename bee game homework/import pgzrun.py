import pgzrun
from time import time
import random
WIDTH=600
HEIGHT=400
#varibiales for game
Listbee=[]
Listlines=[]
nextbee=0
starttime=0
totaltime=0
totalbees=16
def orang():
    global starttime
    for i in range(totalbees):
        bee=Actor("bee.png")
        bee.pos=random.randint(45,555),random.randint(30,370)
        Listbee.append(bee)
    starttime=time()
def draw():
    global totaltime
    screen.blit("flowers.jpg",(0,0))
    fn=1
    for o in Listbee:
        o.draw()
        screen.draw.text(str(fn),(o.pos[0],o.pos[1]+20))
        fn+=1
    for line in Listlines:
        screen.draw.line(line[0],line[1],(0,0,0))
    if nextbee <totalbees:
        totaltime=time() - starttime
        screen.draw.text (str(round(totaltime,1)),(10,10),fontsize=30)
def update():
    pass
def on_mouse_down(pos):
    global nextbee,Listlines
    if nextbee<totalbees:
       if Listbee[nextbee].collidepoint(pos):
        if nextbee:
            Listlines.append((Listbee[nextbee-1].pos,Listbee[nextbee].pos))
        nextbee+=1
       else:
        Listlines=[]
        nextbee=0


orang()
pgzrun.go()