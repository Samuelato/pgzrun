import pgzrun
import time
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
for i in range(totaloranges):
    orange=Actor("orange.png")
    orange.pos=random.randint(45,555),random.randint(30,370)
    Listorange.append(orange)
def draw():
    screen.blit("grass.jpg",(0,0))







pgzrun.go()