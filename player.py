import math
import random
import keyboard
from renderer import HUSCIIRenderer
from particles import Particle, Emitter
from utilites import mapv
from bullets import Bullet

class Player():
    def __init__(self, r:HUSCIIRenderer, x, y):
        self.r = r
        self.x = x
        self.y = y
        self.speed = 0.5

        self.reload_delay = 10
        self.reload_time = 1
        self.bullets = []

        self.particle_delay = 10
        self.particle_timer = 1
        self.emitter = Emitter()
        self.particle_speed = 0.4

        self.sprite = [" | ",
                       "/|\\"]

    def update(self):
        if keyboard.is_pressed("w"):
            self.y -= self.speed * 2/3
        if keyboard.is_pressed("s"):
            self.y += self.speed * 2/3
        if keyboard.is_pressed("a"):
            self.x -= self.speed
        if keyboard.is_pressed("d"):
            self.x += self.speed
        
        if keyboard.is_pressed(" ") and self.reload_time <= 0:
            self.bullets.append(Bullet(self.r, self.x + 1, self.y))
            self.reload_time = self.reload_delay
        else:
            self.reload_time -= 1 

        
        self.particle_timer -= 1
        if self.particle_timer == 0:
            self.particle_timer = self.particle_delay
            a = mapv(random.random(), 0, 1, math.pi/4 + math.pi/8, 3*math.pi/4 - math.pi/8)
            vx, vy = math.cos(a) * self.particle_speed, math.sin(a) * self.particle_speed * 2/3
            self.emitter.add_particle(Particle(self.r, self.x + random.randrange(0, 3), self.y + 2, vx, vy, lifespan=50, chars="#"))
        self.emitter.update()

        for bullet in self.bullets:
            bullet.update()

        self.r.sprite(self.x, self.y, self.sprite)