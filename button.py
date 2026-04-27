import pygame

class Button:
    def __init__(self, alien_game):
        self.screen = alien_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/playbutton.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.blit(self.image, self.rect)