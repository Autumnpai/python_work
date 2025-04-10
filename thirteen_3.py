import sys

import pygame

class Raindrops:
    """Falling raindrops"""

    def __init__(self):
        """Initialize"""
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("It's raining.")
                
        self.screen = pygame.display.set_mode((1200, 800))
        self.drops = pygame.sprite.Group()
        self._create_grid()
    
    def start_rain(self):
        """Start raining."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.screen.fill((135, 206, 235))
            self.drops.update()
            self.drops.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
    
    def _create_grid(self):
        """ Create the grid of drops. """
        spacing = 60
        current_x, current_y = spacing + 30, spacing
        while current_y < (800 - spacing):
            while current_x < (1200 - spacing):
                drop = Drop(self)
                drop.rect.x = current_x
                drop.rect.y = current_y
                self.drops.add(drop)
                current_x += 2 * spacing
            current_x = spacing + 30
            current_y += 2 * spacing


class Drop(pygame.sprite.Sprite):
    """ Represent a single drop."""

    def __init__(self, rd):
        """Initialize"""
        super().__init__()
        self.screen = rd.screen

        # Load the drop image and set its rect attribute.
        self.image = pygame.image.load("drop.png")
        self.rect = self.image.get_rect()
    
    def update(self):
        """ Drops falling down """
        self.rect.y += 1


rd = Raindrops()
rd.start_rain()
        