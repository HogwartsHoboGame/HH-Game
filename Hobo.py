import Tracks
import random
import pygame
from Coord import *


class Hobo(Coord):
    # Initializes a Hobo with a certain health
    def __init__(self, tracks, currentTrack, x, y, screen):
        super().__init__(x, y, 0, 0)
        self.tracks = tracks
        self.currentTrack = currentTrack
        self.screen = screen
        self.random = random.randrange(10)

    # Makes a jump from the current track to another random track
    def update(self):
        if (self.currentTrack < self.tracks.numberOfTracks):
            self.tracks.setEmpty(self.currentTrack)
        if (self.random != self.currentTrack):
            self.tracks.setBusy(self.random)

    def draw(self):
        hobo = pygame.image.load("hobo.png")
        self.screen.blit(hobo, (self.x, self.y))
