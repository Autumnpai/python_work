import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # this line is one of the key lines, it assign the self.screen variable
        # a "Surface" object by calling the pygame.display.set_mode(), so
        # self.screen is not a data, it is an class object which is written by C
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):        
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
            
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    # ai.run_game()
    # print(ai.ship.rect)
    # print(ai.ship.rect.midbottom)
    # print(ai.ship.screen_rect)
    print(ai.screen)