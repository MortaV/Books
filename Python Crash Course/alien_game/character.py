import pygame


class Character:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/character.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.bottomright = self.screen_rect.bottomright

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)