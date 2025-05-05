import pgzrun as pz
from random import randint
import math

#screen size
WIDTH = 800
HEIGHT = 600

#variables
hud_0 = Actor("hud_0")
hud_1 = Actor("hud_1")
hud_2 = Actor("hud_2")
hud_3 = Actor("hud_3")
hud_4 = Actor("hud_4")
hud_5 = Actor("hud_5")
hud_6 = Actor("hud_6")
hud_7 = Actor("hud_7")
hud_8 = Actor("hud_8")
hud_9 = Actor("hud_9")
buttonred = Actor("buttonred")
hud_coins = Actor("hud_coins")
hud_gem_blue = Actor("hud_gem_blue")
hud_gem_green = Actor("hud_gem_green")
hud_gem_red = Actor("hud_gem_red")
hud_gem_yellow = Actor("hud_gem_yellow")
bg_castle = Actor("bg_castle")

#collisions
def on_mouse_down(pos):
    if buttonred.collidepoint(pos):
        randint(1, 10)
        if randint == 1:
            def draw():
                screen.clear
                hud_coins.draw
        if randint == 2:
            def draw():
                screen.clear
                hud_coins.draw
        if randint == 3:
            def draw():
                screen.clear
                hud_gem_blue.draw
        if randint == 4:
            def draw():
                screen.clear
                hud_gem_green.draw
        if randint == 5:
            def draw():
                screen.clear
                hud_gem_red.draw
        if randint == 6:
            def draw():
                screen.clear
                hud_gem_yellow.draw
        if randint == 7:
            def draw():
                screen.clear
                hud_coins.draw
        if randint == 8:
            def draw():
                screen.clear
                hud_coins.draw
        if randint == 9:
            def draw():
                screen.clear
                hud_coins.draw
        if randint == 10:
            def draw():
                screen.clear
                hud_coins.draw          
                
#score tracking
score == 0

def on_mouse_down(pos):
    if buttonred.collidepoint(pos):
        #       print(score +1)
if score == 0:
    def draw():
        screen.clear
        hud_0.draw
if score == 1:
    def draw():
        screen.clear
        hud_1.draw
if score == 2:
    def draw():
        screen.clear
        hud_2.draw
if score == 3:
    def draw():
        screen.clear
        hud_3.draw
if score == 4:
    def draw():
        screen.clear
        hud_4.draw
if score == 5:
    def draw():
        screen.clear
        hud_5.draw
if score == 6:
    def draw():
        screen.clear
        hud_6.draw        
if score == 7:
    def draw():
        screen.clear
        hud_7.draw
if score == 8:
    def draw():
        screen.clear
        hud_8.draw
if score == 9:
    def draw():
        screen.clear
        hud_9.draw

#def draw
def draw():
    screen.fill("silver")
    buttonred.draw
    bg_castle.draw

#positions
buttonred = ("100, 100")

pz.go
