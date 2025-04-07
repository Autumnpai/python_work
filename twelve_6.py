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

        self.plane = Plane(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._events_check()
            self.plane.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(120)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill((100, 100, 240))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.plane.blitme()
        pygame.display.flip()
    
    def _events_check(self):
        """Response to the keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.plane.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.plane.moving_down = True
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.plane.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.plane.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of the bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)


class Plane:
    """A class to manage the plance"""

    def __init__(self, h_game):
        """Initialize"""
        self.screen = h_game.screen
        self.screen_rect = h_game.screen.get_rect()
        self.image = pygame.image.load("plane.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        # make the plane moving to right a little.
        self.rect.left = self.rect.left + 16
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the plane's position based on the movement flag"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 2
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 2
    
    def blitme(self):
        """Draw the plane at its current location."""
        self.screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, h_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = h_game.screen
        self.color = (255, 64, 0)

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 15, 6)
        self.rect.midright = h_game.plane.rect.midright
    
    def update(self):
        """Move the bullet to right of the screen"""
        # Update the exact position of the bullet.
        self.rect.x += 3

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


hg = Horizongame()
hg.run_game()
