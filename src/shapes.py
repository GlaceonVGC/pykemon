import pygame
import color

class Shape(): # interface, strokeOn() to be defined
    def stroke(self, surface: pygame.Surface, color: color.Color) -> None:
        s = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        self.strokeOn(s, color)
        surface.blit(s, (0, 0))

    def draw(self, surface: pygame.Surface, colors: tuple) -> None:
        self.stroke(surface, colors[0])

class Line(Shape):
    def __init__(self, start: tuple, end: tuple):
        self.start = start
        self.end = end

    def strokeOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.line(surface, color.convert(), self.start, self.end)

class ClosedShape(Shape): # interface, strokeOn() and fillOn() to be defined
    def fill(self, surface: pygame.Surface, color: color.Color) -> None:
        s = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        self.fillOn(s, color)
        surface.blit(s, (0, 0))

    def draw(self, surface: pygame.Surface, colors: tuple) -> None:
        # colors: (stroke, fill)
        self.fill(surface, colors[1])
        self.stroke(surface, colors[0])

class Ellipse(ClosedShape):
    def __init__(self, left: int, top: int, width: int, height: int = None):
        self.left = left
        self.top = top
        self.width = width
        self.height = width if height is None else height

    def convert(self) -> tuple:
        return (self.left, self.top, self.width, self.height)
        
    def fillOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.ellipse(surface, color.convert(), self.convert())

    def strokeOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.ellipse(surface, color.convert(), self.convert(), 1)

class Polygon(ClosedShape):
    def __init__(self, *vertice: tuple) -> None:
        self.vertice = vertice

    def fillOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.polygon(surface, color.convert(), self.vertice)

    def strokeOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.polygon(surface, color.convert(), self.vertice, 1)

class Rectangle(Polygon):
    def __init__(self, left: int, top: int, right: int, bottom: int):
        self.left = left
        self.top = top
        self.width = right - left
        self.height = bottom - top

    def convert(self) -> tuple:
        return (self.left, self.top, self.width, self.height)
        
    def fillOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.rect(surface, color.convert(), self.convert())

    def strokeOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.rect(surface, color.convert(), self.convert(), 1)
