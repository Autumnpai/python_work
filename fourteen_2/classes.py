import pygame

class Shooter:
    """The shooter"""

    def __init__(self, bs):
        """Initialize"""
        self.screen = bs.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("shooter.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_up = False
        self.moving_down = False

class Bullet(pygame.sprite.Sprite):
    """The bullet."""

    def __init__(self, *groups):
        super().__init__(*groups)

class Brick:
    """The brick on the right side."""

    def __init__(self):
        pass