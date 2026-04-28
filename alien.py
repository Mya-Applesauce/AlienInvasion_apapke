"""
alien
Ari Papke
code for the enemies
starter code came from Python Crash Course, 3rd Edition by Eric Matthes
04/19/26
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, alien_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings

        self.image = pygame.image.load("images/ufo.png")
        #art created by me: https://www.pixilart.com/art/ufo-sr5z3c040da62baws3
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x