import sys

import pygame

class A_game():
    """Make a blue sky pygame window"""
    def __init__(self):
        """Initialize the class with some attributes"""
        pygame.init()

        self.screen = pygame.display.set_mode((1920, 1080))

blue_sky = A_game()
blue_sky.screen.fill((40, 160, 200))

while True:
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()