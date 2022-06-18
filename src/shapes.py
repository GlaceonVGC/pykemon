import pygame
import color

class Shape():
    def stroke(self, surface: pygame.Surface, color: color.Color) -> None:
        pass

class ClosedShape(Shape):
    def fill(self, surface: pygame.Surface, color: color.Color) -> None:
        pass

    def draw(self, surface: pygame.Surface, colors: tuple) -> None:
        # colors: (fill, stroke)
        self.fill(colors[0])
        self.stroke(colors[1])

class Polygon(ClosedShape):
    def fill(self, surface: pygame.Surface, color: color.Color) -> None:
        pass # TODO

    def stroke(self, surface: pygame.Surface, color: color.Color) -> None:
        pass # TODO

class Rectangle(Polygon):
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def convert(self) -> tuple:
        return (self.left, self.top, self.width, self.height)
        
    def fill(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.rect(surface, color.convert(), self.convert())

    def stroke(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.rect(surface, color.convert(), self.convert(), 1)
