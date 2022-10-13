from installer import install_if_missing
install_if_missing("J:\pymodules", "keyboard")

import keyboard
import time
from renderer import HUSCIIRenderer
from player import Player
from stars import Star

FPS = 60

def main():
    renderer = HUSCIIRenderer()
    player = Player(renderer, renderer.WIDTH//2, renderer.HEIGHT//2)
    stars = []
    for i in range(20):
        stars.append(Star(renderer))

    while True:
        start = time.time()
        
        for star in stars:
            star.update()
        player.update()

        renderer.draw()

        frametime = time.time() - start
        print(f"FPS: {min(1/frametime, FPS):.1f}")
        time.sleep(max(1/FPS - frametime, 0))
        

if __name__ == "__main__":
    main()