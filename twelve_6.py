import sys

import pygame

class Horizongame:
    """Overall class to manage game assets and behaviors"""
    
    def __init__(self):
        """Initialize"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Horizontal Game")

class Plane:
    """A class to manage the plance"""

    def __init__(self, h_game):
        """Initialize"""
        self.screen = h_game.screen
        self.screen_rect = h_game.screen.get_rect()
        
