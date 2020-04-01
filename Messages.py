import pygame
import Game


class Messages():

    def __init__(self, screen_width, screen_height, screen, health):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.health = health

    def set_fonts(self):
        self.small_font = pygame.font.SysFont("arial", 25)
        self.med_font = pygame.font.SysFont("arial", 40)
        self.large_font = pygame.font.SysFont("arial", 80)

    def to_start_screen(self):
        self.screen.fill((0, 0, 0))
        self.to_screen("Welcome to Hogwarts Hobo Game!",
                       (255, 255, 255), -100, "medium")
        self.to_screen(
            "Press S to start the game and Q to quit.", (255, 255, 255), 25)
        pygame.display.update()

    def to_pause_screen(self):
        self.screen.fill((0, 0, 0))
        self.to_screen("Paused", (255, 255, 255), -100, "large")
        self.to_screen(
            "Press C to continue, M to return no main menu or Q to quit.", (255, 255, 255), 25)
        self.to_screen(
            "Health = " + str(self.health), (255, 255, 255), -330, "small")
        pygame.display.update()

    def to_running_screen(self):
        self.to_screen(
            "Health = " + str(self.health), (255, 255, 255), -330, "small")
        pygame.display.update()

    def text_objects(self, text, color, size):
        if size == "small":
            text_surface = self.small_font.render(text, True, color)
        elif size == "medium":
            text_surface = self.med_font.render(text, True, color)
        elif size == "large":
            text_surface = self.large_font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def to_screen(self, msg, color, y_displace=0, size="small"):
        text_surf, text_rect = self.text_objects(msg, color, size)
        text_rect.center = (
            self.screen_width / 2), (self.screen_height / 2) + y_displace
        self.screen.blit(text_surf, text_rect)
