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
		self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.fps = 30
        self.trains = []
        self.tracks = Tracks.Tracks(10, self.screen)
        self.trains.append(Train.Train(60, 30, 300, self.screen, self.fps))
        self.trains.append(Train.Train(120,30, 200, self.screen, self.fps))
        self.tracks.setBusy(0)
        self.tracks.setBusy(1)
		self.is_started = False
		self.is_paused = False
		self.clock = pygame.time.Clock()

    #Draw the scene for the game
    def draw(self):
        self.tracks.drawTracks()
        for train in self.trains:
            train.update()
            train.draw()

	#Start game
	def start(self):
		#start timer
		clock = self.clock
		if self.is_started:
			return
		self.is_started = True
		while self.is_started:
            pygame.time.delay(int(1000/self.fps))
            event = pygame.event.poll()
            self.draw()
            pygame.display.update()
            if event.type == pygame.QUIT:
                run = False
			#other methods to create game

	#Pause game
	def pause(self):
		clock = self.clock
		if not self.is_started:
			return
		self.is_paused = not self.is_paused
		#save game information, pause timer

	#End game
	def stop():
		clock = self.clock
		if not self.is_started:
			return
		self.is_started = False

	#Player loses all health
	def gameover():
		#stop and return timer

	#possibly helper function
	def terminate():
		pygame.quit()
		sys.exit()

def main():
    game = HH_Game(700,700)
    game.start()


if __name__ == '__main__':
    main()
