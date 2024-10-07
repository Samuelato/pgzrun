import pgzrun
import random
TITLE="shooting neymar"
WIDTH=400
HEIGHT=400
mes="this game is made by Samuel\nhave a nice game!"
#actor methoth to create a sprite
ney=Actor("player.png")
def draw():
    screen.clear()
    screen.fill("green")
    ney.draw()
    screen.draw.text(mes,center=(200,21))
def rand():
    ney.x=random.randint(0,400)
    ney.y=random.randint(0,400)
def on_mouse_down(pos):
    global mes
    if ney.collidepoint(pos):
        rand()
        screen.clear()
        mes="good shot!!"
    else:
        mes="have another try"
rand()
pgzrun.go()