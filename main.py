from installer import install_if_missing
install_if_missing("J:\pymodules", "keyboard")

import keyboard
import time
from huscii.renderer import HUSCIIRenderer

FPS = 60

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update():
        if keyboard.is_pressed("w"):
            y -= 1
        if keyboard.is_pressed("s"):
            y += 1
        if keyboard.is_pressed("a"):
            x -= 1
        if keyboard.is_pressed("d"):
            x += 1

    def draw():
        renderer


def setup():
    global renderer
    renderer = HUSCIIRenderer()

def update():
    renderer.rect(10, y, 3, 5)
    
    renderer.draw()


if __name__ == "__main__":
    setup()
    while True:
        update()
        time.sleep(1/FPS)