import pygame

class Color():
    def convert(self) -> pygame.Color:
        return (self.r, self.g, self.b, self.a)

    def alpha(self, a: int):
        return RGBA(self.r, self.g, self.b, a)

    def __repr__(self) -> str:
        return f"color.RGBA({self.r!r}, {self.g!r}, {self.b!r}, {self.a!r})"

def RGBA(r: int, g: int, b: int, a: int = 255) -> Color:
    color = Color()
    color.r = r
    color.g = g
    color.b = b
    color.a = a
    return color

def Gray(rgb: int, a: int = 255) -> Color:
    return RGBA(rgb, rgb, rgb, a)

# TODO: write HSLA algorithm

BLACK = RGBA(0, 0, 0)
RED = RGBA(255, 0, 0)
GREEN = RGBA(0, 255, 0)
YELLOW = RGBA(255, 255, 0)
BLUE = RGBA(0, 0, 255)
MAGENTA = RGBA(255, 0, 255)
CYAN = RGBA(0, 255, 255)
WHITE = RGBA(255, 255, 255)
