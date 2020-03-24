import pygame
from Coord import *


class Tracks(Coord):

    def __init__(self, x, y, width, height, numberOfTracks, screen):
        super().__init__(x, y, width, height)
        self.numberOfTracks = numberOfTracks
        self.tracks = [0] * numberOfTracks
        self.screen = screen

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setBusy(self, track):
        self.tracks[track] = 1

    def setEmpty(self, track):
        self.tracks[track] = 0

    def isEmpty(self, track):
        return (self.tracks[track] == 0)

    def draw(self):

        for track in range(1, self.numberOfTracks+1):
            pygame.draw.rect(self.screen, (150, 150, 150),
                             (track*self.x, self.y, self.width, self.height))

        for line in range(1, self.numberOfTracks+1):
            pygame.draw.line(self.screen, (0, 0, 0),
                             (0, line*self.x), (700, line*self.x), 3)
