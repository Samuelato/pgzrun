import random
import pgzrun
import time
WIDTH=600
HEIGHT=300
thib=Actor("thib.png")
bal=Actor("bal.png")
score=0
gameover=False
def draw():
    screen.blit("soccer field.png",(0,0))
    screen.draw.text("Score:"+ str(score), color="white", topleft=(10,10))
    thib.draw()
    bal.draw()
    if gameover==True:
        screen.fill("black")
        screen.draw.text("game over youre score is ................"+ str(score), color="white", center=(200,50))
def randbal():
    bal.x=random.randint(0,600)
    bal.y=random.randint(0,300)
def update():
    global score
    if keyboard.left:
        thib.x=thib.x-2
    if keyboard.right:
        thib.x=thib.x+2
    if keyboard.up:
        thib.y=thib.y-2
    if keyboard.down:
        thib.y=thib.y+2
    if thib.colliderect(bal):
        score+=1
        randbal()
def go():
    global gameover
    gameover=True
randbal()
clock.schedule(go,18)
pgzrun.go()
