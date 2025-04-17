import sys

import pygame

from classes import Brick, Bullet, Shooter, Button

class Brickshootgame:
    """A side shooting game to test 'START' button."""
    
    def __init__(self):
        """Initialize self and assets of the game."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Brick Shooting")

        self.shooter = Shooter(self)
        self.brick = Brick(self)
        self.bullets = pygame.sprite.Group()
        self.start_button = Button(self, "START")

        self.game_active = False
        self.missing_limit = 2

    def runit(self):
        """Run it!"""
        while True:
            self._check_key_press()
            self.screen.fill((135, 206, 235))
            if self.game_active:
                if (self.shooter.moving_down and 
                    self.shooter.rect.bottom < self.screen.get_rect().bottom):
                    self.shooter.rect.y += 2
                if self.shooter.moving_up and self.shooter.rect.top > 0:
                    self.shooter.rect.y -= 2
                for bullet in self.bullets.sprites():
                    bullet.rect.x += 15
                    if pygame.sprite.spritecollideany(self.brick, self.bullets):
                        self.bullets.remove(bullet)
                    if bullet.rect.right >= self.screen.get_rect().right:
                        self._missing(bullet)
                    pygame.draw.rect(bullet.screen, bullet.color, bullet.rect)
            self.brick.brickmoving()
            self.shooter.blitme()
            pygame.draw.rect(
                self.brick.screen, self.brick.color, self.brick.rect)
            if not self.game_active:
                self.start_button.draw_button()
            pygame.display.flip()

            self.clock.tick(60)
    
    def _missing(self, bullet):
        """Respond to the missing shot."""
        if self.missing_limit > 0:
            self.bullets.remove(bullet)
            self.missing_limit -= 1
        else:
            self.game_active = False
    
    def _fire_bullet(self):
        """Create and update the bullets"""
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.brick.moving_speed *= self.brick.speed_increase_scale

    def _check_key_press(self):
        """Check key and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_UP:
                    self.shooter.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.shooter.moving_down = True
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.shooter.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.shooter.moving_down = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_start_button(mouse_pos)
    
    def _check_start_button(self, mouse_pos):
        """Start a new game when the player clicks the button."""
        button_clicked = self.start_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game.
            self.game_active = True
            self.bullets.empty()
            self.missing_limit = 2
            self.shooter.rect.midleft = self.shooter.screen_rect.midleft
            self.brick.moving_speed = 1


bs = Brickshootgame()
bs.runit()