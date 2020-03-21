import pygame
import Hobo

class Tracks:

    def __init__(self, numberOfTracks, screen):
        self.numberOfTracks = numberOfTracks
        self.tracks = [0] * numberOfTracks
        self.screen = screen

    def getNumberOfTracks(self):
        return self.numberOfTracks
    
    def setBusy(self, track):
        self.tracks[track] = 1

    def setEmpty(self, track):
        self.tracks[track] = 0

    def isEmpty(self, track):
        return (self.tracks[track] == 0)

    def printTracks(self):
        hobo = Hobo.Hobo(5, 0, self.screen)
        trackHeight = 600
        trackWidth = 40
        initY = 30
        initX = 60
        for track in range(1, self.numberOfTracks+1):
            pygame.draw.rect(self.screen, (150, 150,150), (track*initX, initY, trackWidth, trackHeight))
            if not self.isEmpty(track-1):
                hobo.drawHobo((track*initX+20, 615)) 

        for line in range(1, self.numberOfTracks+1):
            pygame.draw.line(self.screen, (0, 0, 0), (0, line*initX), (700, line*initX), 3)

                   
