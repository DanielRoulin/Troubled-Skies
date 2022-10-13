import math
from renderer import HUSCIIRenderer
from utilites import mapv

class Particle():
    def __init__(self, r:HUSCIIRenderer, x, y, vx, vy, lifespan=100, chars="@%*\"\'"):
        self.r = r
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.chars = chars
        self.lifespan = lifespan
        self.age = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy

        self.r.point(self.x, self.y, self.chars[math.floor(mapv(self.age, 0, self.lifespan + 1, 0, len(self.chars)))])
        self.age += 1


class Emitter():
    def __init__(self):
        self.particles = []

    def add_particle(self, p:Particle):
        self.particles.append(p)

    def update(self):
        for i, particle in enumerate(self.particles):
            particle.update()
            if particle.age == particle.lifespan:
                del self.particles[i]
