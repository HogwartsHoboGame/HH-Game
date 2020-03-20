import pygame


Class HH_Game():
	def __init__(self):
		self.is_started = False
		self.is_paused = False
		self.clock = pygame.time.Clock()

	#Start game
	def start(self):
		#start timer
		clock = pygame.time.Clock()
		if self.is_started:
			return
		self.is_started = True
		while True:
			#other methods to create game

	#Pause game
	def pause(self):
		clock = pygame.time.Clock()
		if not self.is_started:
			return
		self.is_paused = not self.is_paused
		#save game information, pause timer

	#End game
	def stop():
		clock = pygame.time.Clock()
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
	pygame.init()
	while True:
		#initialize everything


if __name__ == '__main__':
	main()
