"""
Ship
Ari Papke
code for the player character
starter code came from Python Crash Course, 3rd Edition by Eric Matthes
04/19/26
"""

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, alien_game):
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings
        self.screen_rect = alien_game.screen.get_rect()

        self.image = pygame.image.load("images/spaceship2.png")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)