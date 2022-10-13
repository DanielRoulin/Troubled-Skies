import random
from renderer import HUSCIIRenderer
from utilites import mapv

class Star():
    def __init__(self, r:HUSCIIRenderer):
        self.r = r
        self.reset()
        self.y = random.random() * self.r.HEIGHT

    def reset(self):
        self.speed = mapv(random.random(), 0, 1, 0.1, 0.3)
        self.x = random.random() * self.r.WIDTH
        self.char = random.choice(".")

    def update(self):
        self.y += self.speed
        if self.y > self.r.HEIGHT:
            self.y = 0
            self.reset()

        self.r.point(self.x, self.y, self.char)
