from circleshape import *
from constants import ASTEROID_MIN_RADIUS
from pygame import draw
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = uniform(20, 50)
            random_angle = self.velocity.rotate(angle)
            neg_random_angle = self.velocity.rotate(-1 * angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first = Asteroid(self.position.x, self.position.y, new_radius)
            second = Asteroid(self.position.x, self.position.y, new_radius)
            first.velocity = random_angle * 1.2
            second.velocity = neg_random_angle * 1.2