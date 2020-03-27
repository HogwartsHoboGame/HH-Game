import pygame
import Tracks
import Train
import Hobo
import Player
from Coord import *
import random


class HH_Game():
    def __init__(self, screenWidth, screenHeight):
        pygame.init()
        pygame.display.set_caption("HH GAME")
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screen = pygame.display.set_mode(
            (self.screenWidth, self.screenHeight))
        self.smallfont = pygame.font.SysFont("arial", 25)
        self.medfont = pygame.font.SysFont("arial", 40)
        self.largefont = pygame.font.SysFont("arial", 80)
        self.tracks = Tracks.Tracks(60, 30, 40, 600, 10, self.screen)
        self.tracks.setBusy(0)
        self.tracks.setBusy(1)
        self.tracks.setBusy(4)
        self.tracks.setBusy(6)
        self.fps = 30
        self.speed = 150
        self.hobos = []
        self.addHobos()
        self.trains = []
        self.addTrains()
        self.is_started = False
        self.is_paused = False
        self.clock = pygame.time.Clock()

    def addTrains(self):
        for track in range(1, self.tracks.numberOfTracks+1):
            self.trains.append(Train.Train(
                track-1, track*self.tracks.x, self.tracks.y, self.speed*track/3, self.screen, self.fps))

    def addHobos(self):
        for track in range(1, self.tracks.numberOfTracks+1):
            if not (self.tracks.isEmpty(track-1)):
                self.hobos.append(Hobo.Hobo(
                    self.tracks, track-1, track*self.tracks.x, self.tracks.height, self.screen))

    def removeHobos(self):
        for hobo in self.hobos:
            if (self.tracks.isEmpty(hobo.currentTrack)):
                self.hobos.remove(hobo)

    def getHobo(self, track):
        for hobo in self.hobos:
            if hobo.currentTrack == track:
                return hobo

    def getCurrentTracks(self):
        currentTracks = []
        for hobo in self.hobos:
            currentTracks.append(hobo.currentTrack)
        return currentTracks

    def handleCollision(self):
        for track in self.getCurrentTracks():
            if (self.getHobo(track) != None and self.trains[track].almostIntersect(self.getHobo(track))):
                self.trains[track].y = 40
                self.removeHobos()
                self.addHobos()

    def update(self):
        for train in self.trains:
            train.update()
        for hobo in self.hobos:
            hobo.update()

    # Draw the scene for the game

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tracks.draw()
        for hobo in self.hobos:
            hobo.draw()
        for train in self.trains:
            train.draw()

    # Start game
    def start(self):
        # start timer
        clock = self.clock
        self.display_start_screen()
        while self.is_started:
            pygame.time.delay(int(1000/self.fps))
            self.update()
            self.handleCollision()
            self.draw()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.is_started = False
                    quit()
                if event.type == pygame.KEYDOWN:
                    # press P to pause
                    if event.key == pygame.K_p:
                        self.pause()

    def display_start_screen(self):
        self.is_paused = True
        while self.is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.is_started = True
                        self.is_paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.start_screen()
            pygame.display.update()

    def start_screen(self):
        self.screen.fill((0, 0, 0))
        self.message_to_screen("Welcome to Hogwarts Hobo Game!",
                               (255, 255, 255), -100, "medium")
        self.message_to_screen(
            "Press C to start the game!", (255, 255, 255), 25)

    # Pause game

    def pause(self):
        clock = self.clock
        self.is_paused = True
        while self.is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.is_paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.pause_screen()
            pygame.display.update()

    def pause_screen(self):
        self.screen.fill((0, 0, 0))
        self.message_to_screen("Paused", (255, 255, 255), -100, "large")
        self.message_to_screen(
            "Press C to continue or Q to quit.", (255, 255, 255), 25)

    def text_objects(self, text, color, size):
        if size == "small":
            textSurface = self.smallfont.render(text, True, color)
        elif size == "medium":
            textSurface = self.medfont.render(text, True, color)
        elif size == "large":
            textSurface = self.largefont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def message_to_screen(self, msg, color, y_displace=0, size="small"):
        textSurf, textRect = self.text_objects(msg, color, size)
        textRect.center = (
            self.screenWidth / 2), (self.screenHeight / 2) + y_displace
        self.screen.blit(textSurf, textRect)


def main():
    game = HH_Game(700, 700)
    game.start()


if __name__ == '__main__':
    main()
