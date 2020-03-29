import pygame
import Tracks
import Train
import Hobo
import Player
from Coord import *
import random


class HH_Game():
    def __init__(self, screen_width, screen_height):
        pygame.init()
        pygame.display.set_caption("HH GAME")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.set_fonts()
        self.reset_game()
        self.is_started = False

    def set_fonts(self):
        self.small_font = pygame.font.SysFont("arial", 25)
        self.med_font = pygame.font.SysFont("arial", 40)
        self.large_font = pygame.font.SysFont("arial", 80)

    def reset_game(self):
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
                self.trains[track].y = 40
                self.remove_hobos()
                self.add_hobos()

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
        self.display_start_screen()
        while self.is_started:
            pygame.time.delay(int(1000/self.fps))
            self.update()
            self.handle_collision()
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
                    if event.key == pygame.K_m:
                        self.display_start_screen()

    def display_start_screen(self):
        self.is_paused = True
        while self.is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.reset_game()
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
            "Press S to start the game and Q to quit.", (255, 255, 255), 25)

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
                    elif event.key == pygame.K_m:
                        self.display_start_screen()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            self.pause_screen()
            pygame.display.update()

    def pause_screen(self):
        self.screen.fill((0, 0, 0))
        self.message_to_screen("Paused", (255, 255, 255), -100, "large")
        self.message_to_screen(
            "Press C to continue, M to return no main menu or Q to quit.", (255, 255, 255), 25)

    def text_objects(self, text, color, size):
        if size == "small":
            text_surface = self.small_font.render(text, True, color)
        elif size == "medium":
            text_surface = self.med_font.render(text, True, color)
        elif size == "large":
            text_surface = self.large_font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_to_screen(self, msg, color, y_displace=0, size="small"):
        text_surf, text_rect = self.text_objects(msg, color, size)
        text_rect.center = (
            self.screen_width / 2), (self.screen_height / 2) + y_displace
        self.screen.blit(text_surf, text_rect)


def main():
    game = HH_Game(700, 700)
    game.start()


if __name__ == '__main__':
    main()
