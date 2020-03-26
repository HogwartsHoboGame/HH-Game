import pygame
from Hobo import *


class Player(Hobo):

    def __init__(self, health, tracks, currentTrack, x, y, screen):
        super().__init__(tracks, currentTrack, x, y, 0, 0, screen)
        self.health = health

    def update(self):
        if (self.currentTrack < self.tracks.numberOfTracks):
            self.tracks.setEmpty(self.currentTrack)
            self.tracks.setBusy(self.random)
            self.health -= 1

    # def draw(self):
        # pygame.draw.rect(self.screen, (0, 0, 255),
        #                 (self.x, self.y, self.width, self.height))
