class Settings:
    """ Store all settings for side shooter game."""

    def __init__(self):
        """Initialize"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Bullet settings:
        self.bullet_speed = 3.0
        self.bullet_height = 15
        self.bullet_width = 6
        self.bullet_color = (255, 64, 0)
        self.bullet_allowed = 4

        # Alien settings
        self.alien_speed = 1.5
        self.fleet_forward_speed = 20
        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_direction = -1

        # Plane settings
        self.plane_speed = 1.5
        self.plane_limit = 3