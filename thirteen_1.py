import pygame

class Stargame:
    """Display a grid of stars"""

    def __init__(self):
        """Initialize"""
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Twinkle twinkle little star!')
        self.screen = pygame.display.set_mode((1860, 1020))
        self.stars = pygame.sprite.Group()
        self._create_grid()
            
    def runit(self):
        """Run it"""
        while True:
            self.stars.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def _create_grid(self):
        """Create the grid of stars."""
        image_size = 60
        current_x, current_y = image_size, image_size
        while current_y < (1020 - image_size):
            while current_x < (1860 - image_size):
                star = Star(self)
                star.rect.x = current_x
                star.rect.y = current_y
                self.stars.add(star)
                current_x += 2 * image_size
            current_x = image_size
            current_y += 2 * image_size


class Star(pygame.sprite.Sprite):
    """A class to represent a sinlge star"""
    def __init__(self, sg):
        """Initialize"""
        super().__init__()
        self.screen = sg.screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load("star.png")
        self.rect = self.image.get_rect()


sg = Stargame()
sg.runit()