import pgzrun
import random
WIDTH=600
HEIGHT=370
score=0
basket=Actor("basket.png")
basket.pos=(300,315)
frikandel=Actor("frikandelbroodje.png")
def draw():
    screen.blit("backgroend.jpg",(0,0))
    basket.draw()
    frikandel.draw()
    screen.draw.text("score:"+str(score),center=(40,20))
def update():
    pass
    if keyboard.right:
        basket.x+=10
    if keyboard.left:
        basket.x-=10
    frikandel.y+=4
    if frikandel.y>370:
        frikandel.y=0
        frikandel.x= random.randint(0,600)
    











pgzrun.go()