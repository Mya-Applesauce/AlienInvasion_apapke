"""
button
Ari Papke
code for the play button
starter code came from Python Crash Course, 3rd Edition by Eric Matthes
04/19/26
"""

import pygame

class Button:
    """A class to build buttons for the game."""

    def __init__(self, alien_game):
        """Initialize button attributes."""
        self.screen = alien_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/playbutton.png")
        #art created by me: https://www.pixilart.com/art/play-button-sr5zf0ddde602eaws3
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def draw_button(self):
        """Draw the button to the screen."""
        self.screen.blit(self.image, self.rect)