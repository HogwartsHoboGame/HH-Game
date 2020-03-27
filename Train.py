import pygame
import Tracks
import Game
from Coord import *


class Train(Coord):

    def __init__(self, current_track, x, y, speed, screen, fps):
        super().__init__(x, y, 0, 0)
        self.current_track = current_track
        self.fps = fps
        self.speed = speed
        self.screen = screen
        self.color = (0, 255, 0)

    def draw(self):
        train = pygame.image.load("images/train.png")
        self.screen.blit(train, (self.x, self.y))

    def update(self):
        self.y += self.speed/self.fps
        if (self.y > self.screen.get_height()-130):
            self.y = 40
