import pgzrun
import time
import random
WIDHT=600
HEIGHT=590
#varibles
List=["plastic-bag.png","straw.jpg","bottle.jpg","batery.jpg"]
speedo=7
startspeedo=10
totallevels=7
gameovere=False
gamecompleten=False
items=[]
currentlev=1
def make_items(extraitem):
    newitem=[]
    options=["paper bag.jpg"]+ random.choices(List,k=extraitem)
    random.shuffle(options)
    for i in options:
        item=Actor(i)
        newitem.append(item)
    gap=WIDHT/(len(newitem)+1)
    for index,item in enumerate(newitem):
        item.y=0
        item.x=(index+1)* gap
        animate(item,duration=startspeedo-currentlev,on_finished=game,y=HEIGHT)
    return newitem
def draw():
    screen.blit("background.jpg",(0,0))
    if gameovere:
        screen.draw.text("GAMEOVER!!!!!!!!!",center=(50,50),fontsize=60,color="white")
    for item in items:
        item.draw()
def update():
    global items,currentlev
    if len (items)==0:
        items=make_items(currentlev)

    pass
def game():
    global gameovere
    gameovere=True
def on_mouse_down(pos):
    global items,currentlev,gamecompleten
    for i in items:
        if i.collidepoint(pos):
            if "paper bag" in i.image:
                currentlev,totallevels 
                if currentlev==totallevels:
                    gamecompleten=True
                else:
                    currentlev+=1
                    items.clear()
            else:
                game()



pgzrun.go()
