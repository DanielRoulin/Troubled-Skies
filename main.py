from installer import install_if_missing
install_if_missing("J:\pymodules", "keyboard")

import keyboard
import time
from huscii.renderer import HUSCIIRenderer

def main():
    renderer = HUSCIIRenderer()
    y = 0
    while True:
        if keyboard.is_pressed("w"):
            y -= 1
        if keyboard.is_pressed("s"):
            y += 1

        renderer.rect(10, y, 3, 5)
        
        renderer.draw()
        time.sleep(1/10)


if __name__ == "__main__":
    main()