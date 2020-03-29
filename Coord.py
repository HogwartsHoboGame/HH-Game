import pygame


class Coord:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def almost_intersect(self, other):
        bottom = self.y + 50
        other_top = other.y

        return not (bottom <= other_top-10)

    def intersects(self, other):
        bottom = self.y + 50
        other_top = other.y

        return not (bottom <= other_top)
