import pygame

class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, h_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = h_game.screen
        self.settings = h_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 
                    self.settings.bullet_height, self.settings.bullet_width)
        self.rect.midright = h_game.plane.rect.midright

        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet to right of the screen"""
        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)