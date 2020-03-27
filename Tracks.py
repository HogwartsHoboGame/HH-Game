import pygame
from Coord import *


class Tracks(Coord):

    def __init__(self, x, y, width, height, number_of_tracks, screen):
        super().__init__(x, y, width, height)
        self.number_of_tracks = number_of_tracks
        self.tracks = [0] * number_of_tracks
        self.screen = screen

    def set_busy(self, track):
        self.tracks[track] = 1

    def set_empty(self, track):
        self.tracks[track] = 0

    def is_empty(self, track):
        return (self.tracks[track] == 0)

    def draw(self):
        for track in range(1, self.number_of_tracks+1):
            pygame.draw.rect(self.screen, (150, 150, 150),
                             (track*self.x, self.y, self.width, self.height))

        for line in range(1, self.number_of_tracks+1):
            pygame.draw.line(self.screen, (0, 0, 0),
                             (0, line*self.x), (700, line*self.x), 3)
