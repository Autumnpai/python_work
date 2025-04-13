import sys
from time import sleep

import pygame

from settings import Settings
from plane import Plane
from bullet import Bullet
from alien import Alien
from game_stats import Gamestats

class Horizongame:
    """Overall class to manage game assets and behaviors"""
    
    def __init__(self):
        """Initialize"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Horizontal Game")

        self.plane = Plane(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.stats = Gamestats(self)

        self.game_active = True
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._events_check()
            if self.game_active:
                self.plane.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60) # this changes the speed of the game, 
                                # not only the screen refresh rate. 
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.plane.blitme()
        self.aliens.draw(self.screen)

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
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of the bullets and get rid of old bullets."""
        # Update bullet's positions.
        self.bullets.update()
        # Get rid of the bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bulllet-alien collisions."""
        # Check for any bullets that have hit the aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update the positions of all 
        aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.plane, self.aliens):
            self._plane_hit()
        
        self._check_aliens_leftedge()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width * 4, alien_height
        while current_y < (self.settings.screen_height - 2 * alien_height):
            while current_x < (self.settings.screen_width - alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # Finish a row; reset x value, and increment y value.
            current_x = alien_width * 4
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and put it in the row."""
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Response appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Forward the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_forward_speed
        self.settings.fleet_direction *= -1

    def _plane_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.plane_left > 0:
            self.stats.plane_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.plane.center_plane()
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_leftedge(self):
        for alien in self.aliens.sprites():
            if alien.rect.x <= 0:
                self._plane_hit()
                break


hg = Horizongame()
hg.run_game()
