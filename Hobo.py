import Tracks
import random
import pygame
from Coord import *


class Hobo(Coord):
    # Initializes a Hobo with a certain health
    def __init__(self, tracks, current_track, x, y, screen):
        super().__init__(x, y, 0, 0)
        self.tracks = tracks
        self.current_track = current_track
        self.screen = screen
        self.random = random.randrange(10)

    # Makes a jump from the current track to another random track
    def update(self):
        if (self.current_track < self.tracks.number_of_tracks):
            self.tracks.set_empty(self.current_track)
            self.tracks.set_busy(self.random)

    def draw(self):
        hobo = pygame.image.load("images/hobo.png")
        self.screen.blit(hobo, (self.x, self.y))
