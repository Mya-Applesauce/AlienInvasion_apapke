"""
Settings
Ari Papke
determines the attributes for various objects
starter code came from Python Crash Course, 3rd Edition by Eric Matthes
04/19/26
"""

import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (69, 32, 136)
        self.bg_image = pygame.image.load("images/space.png")
        self.hud_image = pygame.image.load("images/hud3.png")

        self.bg_music = pygame.mixer.music.load("music/invitation.mp3")
        
        self.ship_limit = 3

        self.fleet_drop_speed = 10.0

        self.bullet_image = pygame.image.load("images/bullet.png")
        self.bullets_allowed = 20

        self.speedup_scale = 1.3
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 8
        self.bullet_speed = 5.0
        self.alien_speed = 2.0
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)