import pygame

class Plane:
    """A class to manage the plance"""

    def __init__(self, h_game):
        """Initialize"""
        self.screen = h_game.screen
        self.screen_rect = h_game.screen.get_rect()
        self.image = pygame.image.load("plane.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        # make the plane moving to right a little.
        self.rect.left = self.rect.left
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the plane's position based on the movement flag"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 2
    
    def blitme(self):
        """Draw the plane at its current location."""
        self.screen.blit(self.image, self.rect)