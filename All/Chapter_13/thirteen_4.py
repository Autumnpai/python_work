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
            self._check_keydown()
            self.screen.fill((135, 206, 235))
            self.drops.draw(self.screen)
            self.drops.update()
            pygame.display.flip()
            self.clock.tick(60)
    
    def _check_keydown(self):
        """Check keyboard keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                # Change the speed of the dropping.
                for drop in self.drops:
                    if event.key == pygame.K_UP:
                        drop.speed += 1
                    if event.key == pygame.K_DOWN and drop.speed > 0:
                        drop.speed -= 1
                    if event.key == pygame.K_SPACE:
                        drop.speed = 0
    
    def _create_grid(self):
        """ Create the grid of drops. """
        # Make spacing for vertical 60, and for horizon double/120.
        spacing = 60
        # this variable is for changing starting level. 0 starts from bottom.
        horizon_ratio = 12
        current_x, current_y = spacing + 30, -(horizon_ratio * spacing + 91)
        while current_y < (800 - horizon_ratio * spacing):
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

        # Falling speed
        self.speed = 1
    
    def update(self):
        """ Drops falling down """
        if self.rect.y >= 869:  # check if a drop is READY to go to the top.
            self.rect.y = -91   # change it to the top.
        else:
            self.rect.y += self.speed


rd = Raindrops()
rd.start_rain()
        