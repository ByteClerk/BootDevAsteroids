import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 
                           center=self.position, 
                           radius=self.radius, 
                           width=2,
                           color=pygame.Color("gray30"))
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        offest = random.uniform(20,50)
        vec1 = self.velocity.rotate(offest)
        vec2 = self.velocity.rotate(-offest)
        result_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, radius=result_radius)
        asteroid1.velocity = vec1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, radius=result_radius)
        asteroid2.velocity = vec2 * 1.2