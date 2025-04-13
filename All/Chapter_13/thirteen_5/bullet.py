import pygame

class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, h_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = h_game.screen
        self.color = (255, 64, 0)

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 15, 6)
        self.rect.midright = h_game.plane.rect.midright
    
    def update(self):
        """Move the bullet to right of the screen"""
        # Update the exact position of the bullet.
        self.rect.x += 3

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)