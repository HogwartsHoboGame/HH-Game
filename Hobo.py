import Tracks
import numpy as np

class Hobo:

    # Initializes a Hobo with a certain health
    def __init__(self, health, currentTrack):
        self.health = health
        self.currentTrack = currentTrack
        tracks = Tracks(10)
        self.numberOfTracks = tracks.getNumberOfTracks()

    # Makes a jump from the current track to another random track
    def jump(self):
        # set current track to empty
        tracks.setEmpty(currentTrack)

        #Got random number using Poisson probability
        randomTrack = np.random.poisson(0, self.numberOfTracks)
        
        # Set destination to busy if it's empty
        # if it's not empty, hobo loses health
        if not tracks.isEmpty(randomTrack):
            self.health = health - 1
        else:
            tracks.setBusy(randomTrack)


