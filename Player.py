import pygame
from Hobo import *


class Player(Hobo):

    def __init__(self, health, tracks, current_track, x, y, screen):
        super().__init__(tracks, current_track, x, y, 0, 0, screen)
        self.health = health

    def update(self):
        if (self.current_track < self.tracks.number_of_tracks):
            self.tracks.set_empty(self.current_track)
            self.tracks.set_busy(self.random)
            self.health -= 1

    # def draw(self):
        # pygame.draw.rect(self.screen, (0, 0, 255),
        #                 (self.x, self.y, self.width, self.height))
