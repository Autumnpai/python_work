import sys
import pygame

class Rgame():
    """A game with a rocket moving 4 directions."""
    def __init__(self):
        """Initialize"""
        pygame.init
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1920, 1080))

        self.rocket = Rocket(self)
    
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(120)
               
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill((100, 100, 230))
        self.rocket.blitme()
        pygame.display.flip()
    
    def _check_events(self):
        """Response to the keypresses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Response to the keypresses"""
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        """Response to the key releases."""
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    

class Rocket():
    """The rocket"""
    def __init__(self, rgame):
        """Initialize"""
        # assign the screen of the game backgroudn to the rocket's screen,
        # now they share the same screen/surface.
        self.screen = rgame.screen
        self.rocket_speed = 2
        
        # set the image.
        self.image = pygame.image.load('rocket_small.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
  
    def blitme(self):
        """Draw the rocket at its current location"""
        rgame.screen.blit(self.image, self.rect)
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.rocket_speed
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.rect.x += self.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.rocket_speed
        if self.moving_down and self.rect.bottom < (self.screen.get_rect().bottom + 36):
            self.rect.y += self.rocket_speed


rgame = Rgame()
rgame.run_game()