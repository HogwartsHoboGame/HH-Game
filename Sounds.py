import pygame


class Sounds():

    def __init__(self):
        self.crash_sound = pygame.mixer.Sound("./sounds/crash.wav")

    def background_music(self):
        pygame.mixer.music.load("./sounds/background.ogg")
        pygame.mixer.music.play(-1)

    def trains_music(self):
        pygame.mixer.music.load("./sounds/trains.ogg")
        pygame.mixer.music.play(-1)
