import pygame
import Tracks
import Game
from Coord import *


class Train(Coord):
    # parameters: time it takes for train to pass, and the track its on
    def __init__(self, currentTrack, x, y, speed, screen, fps):
        #self.passTime = passTime
        #self.trackNum = trackNum
        super().__init__(x, y, 0, 0)
        self.currentTrack = currentTrack
        self.fps = fps
        self.speed = speed
        self.screen = screen
        self.color = (0, 255, 0)

    def draw(self):
        # pygame.draw.rect(self.screen, self.color,
        #                 (self.x, self.y, self.width, self.height))
        train = pygame.image.load("train.png")
        self.screen.blit(train, (self.x, self.y))

    def update(self):
        self.y += self.speed/self.fps
        if (self.y > self.screen.get_height()-130):
            self.y = 40
