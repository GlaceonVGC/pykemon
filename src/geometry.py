import pygame
import color

class Shape():
    pass

class ClosedShape(Shape):
    def fill(self, surface: pygame.Surface, color: color.Color) -> None:
        pass

class Polygon(ClosedShape):
    def fill(self, surface: pygame.Surface, color: color.Color) -> None:
        pass # TODO

class Rectangle(Polygon):
    def __init__(self, left: int, top: int, width: int, height: int):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        
    def fill(self, surface: pygame.Surface, color: color.Color) -> None:
        surface.fill(pygame.Color(color.r, color.g, color.b), pygame.Rect(self.left, self.top, self.width, self.height))
