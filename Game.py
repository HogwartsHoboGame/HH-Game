import pygame


Class HH_Game():
	def __init__(self, screenWidth, screenHeight):
		pygame.init()
        	pygame.display.set_caption("HH GAME")
        	self.screenWidth = screenWidth
        	self.screenHeight = screenHeight
		self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
		self.is_started = False
		self.is_paused = False
		self.clock = pygame.time.Clock()

	#Start game
	def start(self):
		#start timer
		clock = self.clock
		if self.is_started:
			return
		self.is_started = True
		while True:
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
    	screen = pygame.display.set_mode((700, 700))
    	tracks = Tracks.Tracks(10, screen)
    	tracks.printTracks()
    	pygame.display.update()
    	run = True
    	while run:
        	pygame.time.delay(100)
        	for event in pygame.event.get():
            		if event.type == pygame.QUIT:
                		run = False
	while True:
		#initialize everything


if __name__ == '__main__':
	main()
