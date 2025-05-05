WIDTH = 800
HEIGHT = 800

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
        apple.x = 300
        apple.y = 200
place_apple()

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("good aim")
        place_apple()
    else:
        print("not the best aim")
        quit()
