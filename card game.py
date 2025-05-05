import pgzrun as pz
from random import randint

#screen size
WIDTH = 450
HEIGHT = 450


    

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
scrooble.pos(250, 230)
trant.pos(250, 230)
foobie.pos(250, 230)
Sranty.pos(250, 230)
bentle.pos(250, 230)
lobur.pos(250, 230)
flamth.pos(250, 230)
vlade.pos(250, 230)
cheat.pos(250, 230)
boxcoin.pos(35, 225)

#draw
def draw():
    screen.fill("grey")
    boxcoin.draw

#randomise
def on_mouse_down():
    if scrooble.collidepoint:
        randint(1, 10)
        if randint == 1: #scrooble
            print("you got a Scrooble!") 
            def draw():
                screen.clear
                scrooble.draw
        elif randint == 2: #trant
            print("you got Trant!")
            def draw():
                screen.clear
                trant.draw
        elif randint == 3: #foobie
            print("you got Foobie!")
            def draw():
                screen.clear
                foobie.draw
        elif randint == 4: #sranty
            print("you got Sranty!")
            def draw():
                screen.clear
                Sranty.draw
        elif randint == 5: #bentle
            print("you got Bentle!")
            def draw():
                screen.clear
                bentle.draw
        elif randint == 6: #lobur
            print("you got Lobur!")
            def draw():
                screen.clear
                lobur.draw
        elif randint == 7: #flamth
            print("you got Flamth!")
            def draw():
                screen.clear
                flamth.draw
        elif randint == 8: #vlade
            print("you got vlade!")
            def draw():
                screen.clear
                vlade.draw
        elif randint == 9: #cheat
            print("you got cheat")
            def draw():
                screen.clear
                cheat.draw
#run
pz.go
