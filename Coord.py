import pygame


class Coord:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersects(self, other):
        left = self.x
        right = self.x + self.width
        top = self.y
        bottom = self.y + self.height

        ohterLeft = other.x
        otherRight = other.x + other.width
        otherTop = other.y
        otherBottom = other.y + other.height

        return not (left <= otherRight or right <= otherLeft or top <= otherBottom or bottom <= otherTop)
