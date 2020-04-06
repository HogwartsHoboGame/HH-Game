import pygame
import Tracks
import Messages
import Sounds
import Train
import Hobo
import Player
import random


class HH_Game():
    def __init__(self, screen_width, screen_height):
        pygame.init()
        # Set screen dimensions
        pygame.display.set_caption("HH GAME")
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        # Set game (number of tracks and hobos)
        self.set_game()
        self.health = 30
        # Set sounds
        self.sounds = Sounds.Sounds()
        self.crash_sound = self.sounds.crash_sound
        self.sounds.background_music()
        # Set messages that will go to the screen
        self.messages = Messages.Messages(
            self.screen_width, self.screen_height, self.screen, self.health)
        self.messages.set_fonts()

    # Set game -- how many tracks, hobos and trains at a given speed.
    def set_game(self):
        self.tracks = Tracks.Tracks(60, 30, 40, 600, 10, self.screen)
        self.tracks.set_busy(0)
        self.tracks.set_busy(1)
        self.tracks.set_busy(8)
        self.tracks.set_busy(9)
        self.fps = 30
        self.speed = 150
        self.hobos = []
        self.add_hobos()
        self.trains = []
        self.add_trains()
        self.init_screen = True
        self.is_started = True
        self.is_paused = True

    # Add trains to the game
    def add_trains(self):
        for track in range(1, self.tracks.number_of_tracks+1):
            self.trains.append(Train.Train(
                track-1, track*self.tracks.x, self.tracks.y, self.speed*track/3, self.screen, self.fps))

    # Add hobos to the game
    def add_hobos(self):
        for track in range(1, self.tracks.number_of_tracks+1):
            if len(self.hobos) >= 4:
                return
            if not (self.tracks.is_empty(track-1)):
                self.hobos.append(Hobo.Hobo(
                    self.tracks, track-1, track*self.tracks.x, self.tracks.height, self.screen))
            else:
                if (self.get_hobo(track-1) != None):
                    self.hobos.remove(self.get_hobo(track-1))

    # Remove hobos if the track should be empty
    def remove_hobos(self):
        for hobo in self.hobos:
            if (self.tracks.is_empty(hobo.current_track)):
                self.hobos.remove(hobo)

    # Returns the hobo in a given track
    def get_hobo(self, track):
        for hobo in self.hobos:
            if hobo.current_track == track:
                return hobo

    # Returns the current tracks of each hobo in the game
    def get_current_tracks(self):
        current_tracks = []
        for hobo in self.hobos:
            current_tracks.append(hobo.current_track)
        return current_tracks

    # Handles collision between trains and hobos
    def handle_collision(self):
        for track in self.get_current_tracks():
            if (self.get_hobo(track) != None and self.trains[track].almost_intersect(self.get_hobo(track))):
                pygame.mixer.Sound.play(self.crash_sound)
                self.trains[track].y = 40
                self.add_hobos()
                self.remove_hobos()
                if self.health > 0:
                    self.health -= 1

    # Updates position of hobos and trains
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
        while self.is_started:
            self.event_loop()
            if self.is_paused and self.init_screen:
                self.messages.to_start_screen()
            elif self.is_paused and (not self.init_screen):
                self.messages.to_pause_screen()
            else:
                self.running()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and self.init_screen:
                    self.run()
                elif event.key == pygame.K_p and not self.init_screen:
                    self.pause()
                elif event.key == pygame.K_c and self.is_paused and not self.init_screen:
                    self.continue_playing()
                elif event.key == pygame.K_m and not self.init_screen:
                    self.main_menu()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

    def running(self):
        pygame.time.delay(int(1000/self.fps))
        self.update()
        self.handle_collision()
        self.draw()
        self.messages.to_screen(
            "Health = " + str(self.health), (255, 255, 255), -330, "small")
        if self.health == 0:
            pygame.quit()
            quit()
        pygame.display.update()

    def run(self):
        self.set_game()
        self.init_screen = False
        self.is_paused = False
        self.sounds.trains_music()

    def pause(self):
        self.sounds.background_music()
        self.is_paused = True
        self.init_screen = False

    def main_menu(self):
        self.sounds.background_music()
        self.is_paused = True
        self.init_screen = True
        self.start()

    def continue_playing(self):
        self.is_paused = False
        self.sounds.trains_music()


def main():
    game = HH_Game(700, 700)
    game.start()


if __name__ == '__main__':
    main()
