from installer import install_if_missing
install_if_missing("J:\pymodules", "keyboard")

import keyboard
import time
from renderer import HUSCIIRenderer

FPS = 60

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 30/FPS

    def update(self):
        if keyboard.is_pressed("w"):
            self.y -= self.speed * 2/3
        if keyboard.is_pressed("s"):
            self.y += self.speed * 2/3
        if keyboard.is_pressed("a"):
            self.x -= self.speed
        if keyboard.is_pressed("d"):
            self.x += self.speed

        renderer.rect(self.x, self.y, 3, 5, "%")
        renderer.draw()
        print(self.x, self.y)


def main():
    global renderer
    renderer = HUSCIIRenderer()
    player = Player(renderer.WIDTH/2, renderer.HEIGHT/2)

    while True:
        start = time.time()
        
        player.update()

        frametime = time.time() - start
        print(f"FPS: {min(1/frametime, FPS):.1f}")
        time.sleep(max(1/FPS - frametime, 0))
        

if __name__ == "__main__":
    main()