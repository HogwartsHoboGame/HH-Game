import pygame
import Tracks
import Train
import Hobo


class HH_Game():
    def __init__(self, screenWidth, screenHeight):
        pygame.init()
        pygame.display.set_caption("HH GAME")
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screen = pygame.display.set_mode(
            (self.screenWidth, self.screenHeight))
        self.tracks = Tracks.Tracks(10, self.screen)
        self.fps = 30
        self.speed = 150
        self.trains = []
        self.addTrains()
        self.is_started = False
        self.is_paused = False
        self.clock = pygame.time.Clock()

    def addTrains(self):
        for track in range(1, self.tracks.numberOfTracks+1):
            self.trains.append(Train.Train(
                track*self.tracks.initX, self.tracks.initY, self.speed*track/3, self.screen, self.fps))

    # Draw the scene for the game

    def draw(self):
        self.tracks.draw()
        for train in self.trains:
            train.update()
            train.draw()

    # Start game
    def start(self):
        # start timer
        clock = self.clock
        while True:
            pygame.time.delay(int(1000/self.fps))
            event = pygame.event.poll()
            self.draw()
            pygame.display.update()
            if event.type == pygame.QUIT:
                break
            # other methods to create game

    # Pause game
    def pause(self):
        clock = self.clock
        if not self.is_started:
            return
        self.is_paused = not self.is_paused
        # save game information, pause timer

    # End game
    def stop():
        clock = self.clock
        if not self.is_started:
            return
        self.is_started = False

    # Player loses all health
    # def gameover():
        # stop and return timer

        # possibly helper function
    def terminate():
        pygame.quit()
        sys.exit()


def main():
    game = HH_Game(700, 700)
    game.start()


if __name__ == '__main__':
    main()
