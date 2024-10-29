import circleShape, pygame

class Asteroid(circleShape.CircleShape):
    def __init__(self, x, y, radius):
        self.x = x,
        self.y = y, 
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)

    def update(self, dt, velocity):
        self.x += (velocity * dt)
        self.y += (velocity * dt)