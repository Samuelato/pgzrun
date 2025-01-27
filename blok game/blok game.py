import random
import itertools
import pgzrun
HEIGHT=400
WIDTH=400
rocket=Actor("rocket.png")
# setting the block positions
listy=[(380,20),(380,380),(20,380),(20,20)]
listie=itertools.cycle(listy)
block=Actor("block.png")
block.pos=(20,20)
rocket.pos=(200,200)
def draw():
    screen.clear()
    block.draw()
    rocket.draw()
def bounce():
    animate(block,"bounce_end",duration=0.5,pos=next((listie)))
def rock():
    #picking random positions
    #
    x=random.randtint(100,400)
    y=random.randtint(100,400)
    rocket.target=x,y
    target_angle=rocket.angle_to(rocket.target)
    target_angle+=360*((rocket.angle-target_angle+180)//360)
    animate(rocket,angle=target_angle,duration=0.01,on_finished=move_ship)
def move_ship():
    anim=animate(rocket,tween="accel_decel",pos=rocket.target,duration=rocket.distance_to(rocket.target)/200,on_finished=rock)
    
bounce()
rock()
clock.schedule_interval(bounce,2)






pgzrun.go()
