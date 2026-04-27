import pygame

class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (69, 32, 136)
        self.bg_image = pygame.image.load("images/space.png")
        
        self.ship_limit = 3

        self.fleet_drop_speed = 10.0

        self.bullet_image = pygame.image.load("images/bullet.png")
        self.bullets_allowed = 20

        self.speedup_scale = 1.3
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 8
        self.bullet_speed = 5.0
        self.alien_speed = 2.0
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)