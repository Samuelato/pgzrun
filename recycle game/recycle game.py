import pgzrun
import time
import random
WIDHT=600
HEIGHT=590
#varibles
List=["plastic-bag.png","straw.jpg","bottle.jpg","batery.webp"]
speedo=7
startspeedo=10
totallevels=7
gameovere=False
gamecompleten=False
items=[]
def make_items(extraitem):
    newitem=[]
    options=["paper bag"]+ random.choices(List)
    random.shuffle(options)

def draw():
    screen.blit("background.jpg",(0,0))
def update():
    pass





pgzrun.go()