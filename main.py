import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

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

    # Create the player at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
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

        # Update game objects
        player.update(dt)

        # Draw game objects
        player.draw(screen)

        # Update the display
        pygame.display.flip()

    # Clean up Pygame resources
    pygame.quit()

if __name__ == "__main__":
    main()
