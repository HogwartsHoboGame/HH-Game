import pygame


Class HH_Game():
	def __init__(self):
		self.is_started = False
		self.is_paused = False

	#Start game
	def start(self):
		if self.is_started:
			return
		self.is_started = True
		#other methods to create game

	#Pause game
	def pause(self):
		if not self.is_started:
			return
		self.is_paused = not self.is_paused
		#save game information

	#End game
	def stop():
		if not self.is_started:
			return
		self.is_started = False

	#Player loses all health
	def gameover():

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
