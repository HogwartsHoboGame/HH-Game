import Tracks
import random
import pygame
from Coord import *


class Hobo(Coord):
    # Initializes a Hobo with a certain health
    def __init__(self, tracks, currentTrack, x, y, width, height, screen):
        super().__init__(x, y, width, height)
        self.tracks = tracks
        self.currentTrack = currentTrack
        self.screen = screen
        self.random = random.randrange(10)

    # Makes a jump from the current track to another random track
    def update(self):
        if (self.currentTrack < self.tracks.numberOfTracks):
            self.tracks.setEmpty(self.currentTrack)
            self.tracks.setBusy(self.random)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))
