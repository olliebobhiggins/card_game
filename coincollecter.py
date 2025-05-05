import pgzrun as pz
from random import randint


WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

alien = Actor("alien")
alien.pos = 100, 100

hud_coins = Actor("hud_coins")
hud_coins.pos = 200, 200

def draw():
    screen.fill("green")
    alien.draw()
    hud_coins.draw()
    screen.draw.text("score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_hud_coin():
    hud_coins.x = randint(20, 300)
    hud_coins.y = randint(20, 300)



def time_up():
    global game_over
    game_over = True


    
def update():
    global score

    if keyboard.left:
        alien.x = alien.x - 5
    elif keyboard.right:
        alien.x = alien.x + 5
    elif keyboard.up:
        alien.y = alien.y - 5
    elif keyboard.down:
        alien.y = alien.y + 5
        
    hud_coins_collected = alien.colliderect(hud_coins)
        

    if hud_coins_collected:
        score = score + 1
        place_hud_coins()

clock.schedule(time_up, 7.0)
place_hud_coin()

pz.go
