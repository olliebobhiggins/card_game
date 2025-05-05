from random import randint
import pgzrun as pz
WIDTH = 400
HEIGHT = 400
game_over = False
alien = Actor("alien")
alien.pos = 100, 100

hud_coins = Actor("hud_coins")
hud_coins.pos = 200, 200

def draw():
    screen.fill("green yellow")
    alien.draw
    hud_coins.draw
    screen.draw.text("score: " + str(score), color="slate grey", topleft=(10, 10))

if game_over:
    screen.fill("pink")
    screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_hud_coin():
    hud_coin.x = randint(00, 400)
    hud_coin.y = randint(00, 400)

def update():
    place_hud_coin()

def time_up():
    global game_over
    game_over = True
    clock.schedule(time_up, 7.0)
    place_hud_coin()

def update():
    global score

    if keyboard.left:
        fox.x = fox.x - 5
    elif keyboard.right:
        fox.x = fox.x + 5
    elif keyboard.up:
        fox.y = fox.y - 5
    elif keyboard.down:
        fox.y = fox.y + 5

    #if hud_coins_collected == fox.colliderect(hud_coin):
        

    if hud_coin_collected:
        score = score + 1
        place_hud_coins()

pz.go
