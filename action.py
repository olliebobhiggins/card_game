import pgzrun as pz
from random import randint

#screen size
WIDTH = 500
HEIGHT = 500

#variables
hud_gem_blue = Actor("hud_gem_blue")
hud_coins = Actor("hud_coins")
p3_front = Actor("p3_front")

#draw
def draw():
    p3_front.draw
def on_mouse_down():

    if p3_front.collidepoint(pos):
        def draw():
            screen.fill("green")
            hud_coins.draw
            

#move
if keyboard.left:
    p3_front.x = p3_front.x - 2
elif keyboard.right:
    p3_front.x = p3_front.x + 2
elif keyboard.up:
    p3_front.y = p3_front.y - 2
elif keyboard.down:
    p3_front.y = p3_front.y + 2

#position
p3_front.pos = 250, 250
hud_coins.pos = 230, 250

#update
def update():
    

pz.go
