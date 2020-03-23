import pygame 
import Tracks
import Game

class Train():
        #parameters: time it takes for train to pass, and the track its on
    def __init__(self, x, y, speed, screen, fps):
            #self.passTime = passTime
            #self.trackNum = trackNum
            self.fps = fps
            self.speed = speed
            self.screen = screen
            self.color = (0, 255, 0)
            self.x = x
            self.y = y
            self.width = 40
            self.height = 60


    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    
    def update(self):
        self.y += self.speed/self.fps
        if (self.y > self.screen.get_height()-130):
            self.y = 40
        



