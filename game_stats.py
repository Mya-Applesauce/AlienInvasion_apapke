"""
game stats
Ari Papke
stores stats
starter code came from Python Crash Course, 3rd Edition by Eric Matthes
04/19/26
"""

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, alien_game):
        """Initialize statistics."""
        self.settings = alien_game.settings
        self.reset_stats()

        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1