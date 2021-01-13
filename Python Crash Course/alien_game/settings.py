class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (250, 219, 216)

        # Ship settings
        self.ship_speed = 1
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 20

        # Star Settings
        self.star_number = 20

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
