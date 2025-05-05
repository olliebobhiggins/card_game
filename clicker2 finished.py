
from random import randint
import pgzrun

# Initialize game window size
WIDTH = 800
HEIGHT = 600

# Initialize game variables
apple = Actor("alien")

coin = Actor("hud_coins")
coin.pos = 200, 200

score = 0


 #apple placement
def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)


def updatescore():
    global score

    score += 1
    print("Score: " + str(score))
    

def draw():
    """Draw function that runs every frame"""
    screen.fill("white")  # Fill screen with black
    screen.draw.text(f"Score: {score}", center=(400, 100), fontsize=60, color="red")  # Draw the score
    apple.draw()
    coin.draw()

def place_coin():
    coin.x = randint(20, 600)
    coin.y = randint(20, 600)


def update():
    global score

    if keyboard.left:
        apple.x = apple.x - 10
    elif keyboard.right:
        apple.x = apple.x + 10
    elif keyboard.up:
        apple.y = apple.y - 10
    elif keyboard.down:
        apple.y = apple.y + 10
        
    coin_collected = apple.colliderect(coin)

    if coin_collected:
        score = score + 1
        place_coin()

#shooting
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("nice shot!")
        updatescore()
        place_apple()
    else:
        print("you suck at this")
     #   quit()


pgzrun.go()  # Start the game 
