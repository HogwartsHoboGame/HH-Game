import pygame


class Coord:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def almostIntersect(self, other):
        left = self.x
        right = self.x + self.width
        top = self.y
        bottom = self.y + self.height

        otherLeft = other.x
        otherRight = other.x + other.width
        otherTop = other.y
        otherBottom = other.y + other.height

        return not (bottom <= otherTop-10)
