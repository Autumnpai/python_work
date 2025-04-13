class Gamestats:
    """Store the changing statistics in the horizonal game"""

    def __init__(self, hg_game):
        """Initialization"""
        self.settings = hg_game.settings
        self.plane_left = hg_game.settings.plane_limit