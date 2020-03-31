import pygame
import Tracks
import Messages
import Sounds
import Train
import Hobo
import Player
from Coord import *
import random


class HH_Game():
    def __init__(self, screen_width, screen_height):
        pygame.init()
        pygame.display.set_caption("HH GAME")
        self.sounds = Sounds.Sounds()
        self.crash_sound = self.sounds.crash_sound
        self.sounds.background_music()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.set_game()
        self.health = 30
        self.messages = Messages.Messages(
            self.screen_width, self.screen_height, self.screen, self.health)
        self.messages.set_fonts()
        self.is_started = False

    def set_game(self):
        self.tracks = Tracks.Tracks(60, 30, 40, 600, 10, self.screen)
        self.tracks.set_busy(0)
        self.tracks.set_busy(1)
        self.tracks.set_busy(4)
        self.tracks.set_busy(6)
        self.fps = 30
        self.speed = 150
        self.hobos = []
        self.add_hobos()
        self.trains = []
        self.add_trains()
        self.is_started = True
        self.is_paused = False

    def add_trains(self):
        for track in range(1, self.tracks.number_of_tracks+1):
            self.trains.append(Train.Train(
                track-1, track*self.tracks.x, self.tracks.y, self.speed*track/3, self.screen, self.fps))

    def add_hobos(self):
        for track in range(1, self.tracks.number_of_tracks+1):
            if not (self.tracks.is_empty(track-1)):
                self.hobos.append(Hobo.Hobo(
                    self.tracks, track-1, track*self.tracks.x, self.tracks.height, self.screen))

    def remove_hobos(self):
        for hobo in self.hobos:
            if (self.tracks.is_empty(hobo.current_track)):
                self.hobos.remove(hobo)

    def get_hobo(self, track):
        for hobo in self.hobos:
            if hobo.current_track == track:
                return hobo

    def get_current_tracks(self):
        current_tracks = []
        for hobo in self.hobos:
            current_tracks.append(hobo.current_track)
        return current_tracks

    def handle_collision(self):
        for track in self.get_current_tracks():
            if (self.get_hobo(track) != None and self.trains[track].almost_intersect(self.get_hobo(track))):
                pygame.mixer.Sound.play(self.crash_sound)
                self.trains[track].y = 40
                self.remove_hobos()
                self.add_hobos()
                if self.health > 0:
                    self.health -= 1

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
        self.display_start_screen()
        while self.is_started:
            pygame.time.delay(int(1000/self.fps))
            self.update()
            self.handle_collision()
            self.draw()
            self.messages.message_to_screen(
                "Health = " + str(self.health), (255, 255, 255), -330, "small")
            if self.health == 0:
                self.is_started = False
                quit()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.is_started = False
                    quit()
                if event.type == pygame.KEYDOWN:
                    # press P to pause
                    if event.key == pygame.K_p:
                        self.sounds.background_music()
                        self.pause()
                    if event.key == pygame.K_m:
                        self.sounds.background_music()
                        self.display_start_screen()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

    def display_start_screen(self):
        self.is_paused = True
        while self.is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.set_game()
                        self.sounds.trains_music()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.messages.start_screen()
            pygame.display.update()

    # Pause game
    def pause(self):
        self.is_paused = True
        while self.is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.is_paused = False
                        self.sounds.trains_music()
                    elif event.key == pygame.K_m:
                        self.sounds.background_music()
                        self.display_start_screen()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.messages.pause_screen()
            pygame.display.update()


def main():
    game = HH_Game(700, 700)
    game.start()


if __name__ == '__main__':
    main()
