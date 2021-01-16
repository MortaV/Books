class GameStats:
    """Tracking statsitics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initializa statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """Initializa statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
