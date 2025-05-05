import pgzrun as pz
import math

#screen size
HEIGHT = 400
WIDTH = 400

#box
box = []
size = 160
score = 0

def on_mouse_dow(pos):
    if box.collidepoint(pos):
        score =+ 1
    else:
        print("click")
        
#draw
def draw():
    screen.fill("green") #change to show different colour
    screen.draw.text("close",topleft=(10, 30), fontsize=50)
    
#close
def on_mouse_dowm(pos):
    if "close".collidepoint(pos):
        quit()

pz.go
