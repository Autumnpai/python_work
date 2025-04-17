import pygame

class Shooter:
    """The shooter"""

    def __init__(self, bs):
        """Initialize"""
        self.screen = bs.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("shooter.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self):
        """Draw the shooter at its current location"""
        self.screen.blit(self.image, self.rect)


class Bullet(pygame.sprite.Sprite):
    """The bullet."""

    def __init__(self, bs):
        super().__init__()
        self.screen = bs.screen
        self.color = (255, 64, 0)
        self.rect = pygame.Rect(0, 0, 8, 4)
        self.rect.x = bs.shooter.rect.x + 120
        self.rect.y = bs.shooter.rect.y + 72


class Brick:
    """The brick on the right side."""

    def __init__(self, bs):
        """Create a ractangle on the right side."""
        self.screen = bs.screen
        self.color = (0, 0, 139)  # Dark blue
        self.rect = pygame.Rect(1100, 0, 100, 200)
        self.movingdirction = 1
    
    def brickmoving(self):
        """Keep moving the brick up and down."""
        self.rect.y += 3 * self.movingdirction
        if self.rect.y <= 0 or self.rect.y >= 600:
            self.movingdirction *= -1


class Button:
    """A class to build buttons."""

    def __init__(self, bs, msg):
        """Initialize attributes."""
        self.screen = bs.screen
        self.screen_rect = self.screen.get_rect()

        # Set dementions and properties of the button.
        self.width, self.height = 200, 60
        self.button_color = (200, 0, 0)
        self.text_color = (0, 255, 255)
        self.font = pygame.font.SysFont(None, 64)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)