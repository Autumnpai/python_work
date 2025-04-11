import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ss_game):
        """Initialize"""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = 0 # 3 * self.rect.width
        self.rect.y = 0 # self.rect.height

        # Store the alien's exact horizontal position.
        # self.y = float(self.rect.y)

    def update(self):
        """Move the alien to the top or bottom."""
        self.rect.y += self.settings.alien_speed * self.settings.fleet_direction
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)