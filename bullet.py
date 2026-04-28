"""
Bullet
Ari Papke
code for the bullets
starter code came from Python Crash Course, 3rd Edition by Eric Matthes
04/19/26
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, alien_game):
        super().__init__()
        self.screen = alien_game.screen
        self.settings = alien_game.settings
        self.screen_rect = alien_game.screen.get_rect()

        self.image = self.settings.bullet_image

        self.rect = self.image.get_rect()
        self.rect.midtop = alien_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
