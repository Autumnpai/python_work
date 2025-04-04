import sys

import pygame

class Showpicture:
    """The background of the picture."""
    def __init__(self):
        """Initialize"""
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.pic = Picture(self)
    
    def runit(self):
        """run it"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((240, 100, 100))
            self.pic.blitme()
            pygame.display.flip() 

class Picture:
    """The picture to show"""
    def __init__(self, background):
        """Initialize"""
        self.screen = background.screen
        self.screen_rect = background.screen.get_rect()
        self.image = pygame.image.load('claire.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sp = Showpicture()
    sp.runit()
"""
    print(sp.pic.rect)
    print(sp.pic.rect.center)
    print(sp.pic.screen_rect)
    print(sp.screen)
"""