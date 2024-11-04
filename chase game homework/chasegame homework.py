import random
import pgzrun
import time
WIDTH=600
HEIGHT=400
basketbal=Actor("basketbal.png")
lebron=Actor("lebron.png")
score=0
gameover=False
def draw():
    screen.blit("field basketbal.webp",(0,0))
    screen.draw.text("Score:"+ str(score), color="white", topleft=(10,10))
    lebron.draw()
    basketbal.draw()
    if gameover==True:
        screen.fill("black")
        screen.draw.text("game over youre score is ..."+ str(score), color="white", center=(200,50))
def randbal():
    basketbal.x=random.randint(0,600)
    basketbal.y=random.randint(0,300)
    




pgzrun.go()