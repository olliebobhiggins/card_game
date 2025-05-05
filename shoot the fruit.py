from random import randint
import pgzrun

apple = Actor("boxcoin")

#screen size
WIDTH = 400
HEIGHT = 400

#apple placement
def place_apple():
    apple.x = randint(10, 400)
    apple.y = randint(10, 400)


place_apple()

#def draw
def draw():
    screen.fill("green")
    apple.draw()


#shooting
#def on_mouse_down(pos):
#    if apple.collidepoint(pos):
#        print("nice shot!")
#        place_apple()
#    else:
 #       print("you suck at this")
 #       quit()


#

pgzrun.go
