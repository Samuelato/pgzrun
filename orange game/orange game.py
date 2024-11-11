import pgzrun
from time import time
import random
WIDTH=600
HEIGHT=400
#varibiales for game
Listorange=[]
Listlines=[]
nextorange=0
starttime=0
totaltime=0
totaloranges=11
def orang():
    global starttime
    for i in range(totaloranges):
        orange=Actor("orange.png")
        orange.pos=random.randint(45,555),random.randint(30,370)
        Listorange.append(orange)
    starttime=time()
def draw():
    global totaltime
    screen.blit("grass.jpg",(0,0))
    fn=1
    for o in Listorange:
        o.draw()
        screen.draw.text(str(fn),(o.pos[0],o.pos[1]+20))
        fn+=1
    for u in Listlines:
        screen.draw.lines(u[0],u[1],(0,0,0))
    if nextorange <totaloranges:
        totaltime=time() - starttime
        screen.draw.text (str(round(totaltime,1)),(10,10),fontsize=30)
def update():
    pass
def on_mouse_down(pos):
    global nextorange,Listlines
    if nextorange<totaloranges:
       if Listorange[nextorange].collidepoint(pos):
        if nextorange:
            Listlines.append((Listorange[nextorange-1].pos,Listorange[nextorange].pos))
        nextorange+1

        




orang()
pgzrun.go()
