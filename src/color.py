import pygame

class Color():
    def convert(self) -> pygame.Color:
        return (self.r, self.g, self.b, self.a)

def RGBA(r: int, g: int, b: int, a: int = 255) -> Color:
    color = Color()
    color.r = r
    color.g = g
    color.b = b
    color.a = a
    return color

# TODO: write HSLA algorithm

BLACK = RGBA(0, 0, 0)
RED = RGBA(255, 0, 0)
GREEN = RGBA(0, 255, 0)
YELLOW = RGBA(255, 255, 0)
BLUE = RGBA(0, 0, 255)
MAGENTA = RGBA(255, 0, 255)
CYAN = RGBA(0, 255, 255)
WHITE = RGBA(255, 255, 255)
