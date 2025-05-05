import pgzrun as zr
import random as rand

#Variables
boxCoin = Actor("boxcoin")
hud_coins = Actor("hud_coins")
#Positions
boxCoin.pos = (00, 00)
hud_coins.pos = (00, -15)


#Screen size
WIDTH = 400
HEIGHT = 400          

#Block
def draw():
    screen.fill("green")
    boxCoin.draw()

#Randimise
def on_mouse_down(pos):
     if boxCoin.collidepoint(pos):
         rand_number = rand.randint(1, 10)
     if rand_number == 1:
         def draw():
                 screen.fill("green")
                 boxCoin.draw()
                 hud_coins.draw()
        

        




zr.go
