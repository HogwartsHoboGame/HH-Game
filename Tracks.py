import pygame
from Hobo import *


class Tracks:

    def __init__(self, numberOfTracks, screen):
        self.numberOfTracks = numberOfTracks
        self.tracks = [0] * numberOfTracks
        self.screen = screen
        self.height = 600
        self.width = 40
        self.initY = 30
        self.initX = 60

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
                             (track*self.initX, self.initY, self.width, self.height))

        for line in range(1, self.numberOfTracks+1):
            pygame.draw.line(self.screen, (0, 0, 0),
                             (0, line*self.initX), (700, line*self.initX), 3)
