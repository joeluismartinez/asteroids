import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Constants
BLACK = (0, 0, 0)

def main() -> None:
    """Main function to run the game."""
    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Print game information
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Define updatable and drawable groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
   

    # Create the player at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Initialize a new AsteroidField object
    AsteroidField()
    
    # Main game loop
    running = True
    while running:
        # Calculate delta time (time since last frame)
        dt = clock.tick(60) / 1000  # 60 FPS, convert to seconds

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BLACK)  # Fill with black color

        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                running = False
                break
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.kill()

        # Update the display
        pygame.display.flip()

    # Clean up Pygame resources
    pygame.quit()

if __name__ == "__main__":
    main()
