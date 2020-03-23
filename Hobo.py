import Tracks
import numpy as np
import pygame


class Hobo:

    # Initializes a Hobo with a certain health
    def __init__(self, health, currentTrack, screen):
        self.health = health
        self.currentTrack = currentTrack
        #tracks = Tracks.Tracks(10)
        #self.numberOfTracks = tracks.getNumberOfTracks()
        self.screen = screen

    # Makes a jump from the current track to another random track
    def jump(self):
        # set current track to empty
        tracks.setEmpty(currentTrack)

        # Got random number using Poisson probability
        randomTrack = np.random.poisson(0, self.numberOfTracks)

        # Set destination to busy if it's empty
        # if it's not empty, hobo loses health   --------> need to implement an
        # incoming train, hobo only lose health if it gets hit
        if not tracks.isEmpty(randomTrack):
            self.health = health - 1
        else:
            tracks.setBusy(randomTrack)

    def draw(self, center):
        if not self.isEmpty(track - 1):
            hobo.draw((track * self.initX + 20, 615))
            pygame.draw.circle(self.screen, (255, 40, 70), center, 15, 3)
