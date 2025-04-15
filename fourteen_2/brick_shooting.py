import sys

import pygame

class Brickshoot:
    """A side shooting game to test 'START' button."""
    
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Brick Shooting")

    def runit(self):
        """Run it!"""
        while True:
            self.clock.tick(60)

