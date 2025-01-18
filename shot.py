from constants import *
from circleshape import *
from pygame import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,SHOT_RADIUS)
    
    def draw(self, screen):
        draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt