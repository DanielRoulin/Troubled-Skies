import random
import math



class Ennemy():
    def __init__(self, r, bullets, x, y):
        self.r = r
        self.bu
        self.x = x
        self.y = y

# ___
# O_O
# / \
class Bomber():
    def __init__(self, r, e, x, y):
        self.r = r
        self.x = x
        self.y = y

        self.t = 0
        self.next_drop = random.randrange(60, 300)

    def update(self):
        self.x = math.cos(self.t/60)*60

        if self.next_drop == 0:
            


