class Settings:
    """ Store all settings for side shooter game."""

    def __init__(self):
        """Initialize"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Bullet settings:
        self.bullet_allowed = 4

        # Alien settings

        # this number can't be <= 0.5, float problem will happen. It is likely 
        # Rect only accept integer, if <=0.5, self.rect.y in Alien(Sprite) class
        # will accept 0 only, the aliens will stop moving.
        self.alien_speed = 1 
        self.fleet_forward_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1