import pygame

class Color():
    @staticmethod
    def RGB(r: int, g: int, b: int):
        color = Color()
        color.r = r
        color.g = g
        color.b = b
        return color

    @staticmethod
    def HSL(h: int, s: int, l: int):
        # TODO: add HSL algorithm
        return Color()

    def convert(self) -> pygame.Color:
        return pygame.Color(self.r, self.g, self.b)
