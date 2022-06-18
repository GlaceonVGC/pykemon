import pygame
import color

class Shape():
    def stroke(self, surface: pygame.Surface, color: color.Color) -> None:
        s = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        self.strokeOn(s, color)
        surface.blit(s, (0, 0))

class ClosedShape(Shape):
    def fill(self, surface: pygame.Surface, color: color.Color) -> None:
        s = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        self.fillOn(s, color)
        surface.blit(s, (0, 0))

    def draw(self, surface: pygame.Surface, colors: tuple) -> None:
        # colors: (fill, stroke)
        self.fill(colors[0])
        self.stroke(colors[1])

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
    def fillOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pass # TODO

    def strokeOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pass # TODO

class Rectangle(Polygon):
    def __init__(self, left: int, top: int, width: int, height: int = None):
        self.left = left
        self.top = top
        self.width = width
        self.height = width if height is None else height

    def convert(self) -> tuple:
        return (self.left, self.top, self.width, self.height)
        
    def fillOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.rect(surface, color.convert(), self.convert())

    def strokeOn(self, surface: pygame.Surface, color: color.Color) -> None:
        pygame.draw.rect(surface, color.convert(), self.convert(), 1)
