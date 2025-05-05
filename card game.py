import pgzrun as pz
from random import randint

#screen size
WIDTH = 800
HEIGHT = 600


    

#variables
boxcoin = Actor("boxcoin")
scrooble = Actor("scrooble")
trant = Actor("trant")
foobie = Actor("foobie")
Sranty = Actor("sranty")
bentle = Actor("bentle")
lobur = Actor("lobur")
flamth = Actor("flamth")
vlade = Actor("vlade")
cheat = Actor("cheat")

#positions
scrooble.pos = (250, 230)
trant.pos = (250, 230)
foobie.pos = (250, 230)
Sranty.pos = (250, 230)
bentle.pos = (250, 230)
lobur.pos = (250, 230)
flamth.pos = (250, 230)
vlade.pos = (250, 230)
cheat.pos = (250, 230)
boxcoin.pos = (35, 225)

#draw
def draw():
    screen.fill("grey")
    boxcoin.draw

current_actor = None  # Add this at the top of your script

def draw():
    screen.fill("grey")
    boxcoin.draw()
    if current_actor:
        current_actor.draw()

def on_mouse_down(pos):
    global current_actor
    if boxcoin.collidepoint(pos):  # Check if the click is on boxcoin
        result = randint(1, 10)
        if result == 1:
            print("You got a Scrooble!")
            current_actor = scrooble
        elif result == 2:
            print("You got Trant!")
            current_actor = trant
        elif result == 3:
            print("You got Foobie!")
            current_actor = foobie
        elif result == 4:
            print("You got Sranty!")
            current_actor = Sranty
        elif result == 5:
            print("You got Bentle!")
            current_actor = bentle
        elif result == 6:
            print("You got Lobur!")
            current_actor = lobur
        elif result == 7:
            print("You got Flamth!")
            current_actor = flamth
        elif result == 8:
            print("You got Vlade!")
            current_actor = vlade
        elif result == 9:
            print("You got Cheat!")
            current_actor = cheat
    else:
        print("Click was not on boxcoin.")
#run
pz.go()
