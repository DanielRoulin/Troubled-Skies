from renderer import HUSCIIRenderer

class Bullet():
    def __init__(self, r:HUSCIIRenderer, x, y):
        self.r = r
        self.x = x
        self.y = y
        self.speed -= 0.75

    def update(self):
        self.y += self.speed

        self.r.point(self.x, self.y, "!")


class Bomb():
    def __init__(self, r:HUSCIIRenderer, x, y):
        self.r = r
        self.x = x
        self.y = y
        self.speed = -0.1
        self.acc = -0.05

    def update(self):
        self.y += self.speed
        self.speed += self.acc

        self.r.point(self.x, self.y, "@")