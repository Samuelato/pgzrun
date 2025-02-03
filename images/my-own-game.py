import random
import time
import pgzrun
WIDTH=600
HEIGHT=300
basketbal=Actor("basketball.png")
jordan=Actor("jordan.png")
score=0
gameover=False
def draw():
    screen.blit("court.jpg",(0,0))
    screen.draw.text("Score:"+ str(score), color="white", topleft=(10,10))
    basketbal.draw()
    jordan.draw()
    if gameover==True:
        screen.fill("black")
        screen.draw.text("game over youre score is ................"+ str(score), color="white", center=(200,50))
def basketball():
    basketbal.x=random.randint(0,600)
    basketbal.y=random.randint(0,300)
def update():
    global score
    if keyboard.left:
        jordan.x=jordan.x-2
    if keyboard.right:
        jordan.x=jordan.x+2
    if keyboard.down:
        jordan.y=jordan.y+2
    if keyboard.up:
        jordan.y=jordan.y-2
    


pgzrun.go()