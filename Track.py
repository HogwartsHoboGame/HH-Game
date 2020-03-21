class Tracks:

    def __init__(self, numberOfTracks):
        self.numberOfTracks = numberOfTracks
        self.tracks = [0] * numberOfTracks

    def setBusy(self, track):
        self.tracks[track] = 1

    def setEmpty(self, track):
        self.tracks[track] = 0

    def isEmpty(self, track):
        return (self.tracks[track] == 0)

    def printTracks(self):
        for track in self.tracks:
            print (" | " + str(track) + " | ", end =" ")
