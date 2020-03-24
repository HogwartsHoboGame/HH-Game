from Tracks import *
import numpy as np
import pygame
from Coord import *


class Hobo(Coord):
    # Initializes a Hobo with a certain health
    def __init__(self, x, y, width, height, currentTrack, screen):
        super().__init__(x, y, width, height)
        #self.health = health
        self.currentTrack = currentTrack
        #tracks = Tracks.Tracks(10)
        #self.numberOfTracks = tracks.getNumberOfTracks()
        self.screen = screen

    # Makes a jump from the current track to another random track
    # def jump(self):
        # set current track to empty
       # tracks.setEmpty(self.currentTrack)

        # Got random number using Poisson probability
        #randomTrack = np.random.poisson(0, self.numberOfTracks)

        # Set destination to busy if it's empty
        # if it's not empty, hobo loses health   --------> need to implement an
        # incoming train, hobo only lose health if it gets hit
        # if not tracks.isEmpty(randomTrack):
        #   self.health = health - 1
        # else:
        #    tracks.setBusy(randomTrack)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))
