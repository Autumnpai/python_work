import sys

import pygame

class Keyevents:
    """Key press events"""
    def __init__(self):
        """Initialize"""
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Keysw')

    def run_it(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    if event.key == pygame.K_q:
                        sys.exit()
            self.clock.tick(120)
            pygame.display.flip()
                        

ke = Keyevents()
ke.run_it()