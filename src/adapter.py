import sys
import typing
import pygame
import align
import archive
import color
import config
import draw
import shapes

# adapter for pygame.time.get_ticks
# varible ticks is to be changed in function new_frame,
# so that get_tick() would be the same within one frame
ticks = 0
def get_tick() -> int:
    return ticks

mouseX, mouseY = (0, 0)

# adapter for pygame.font.Font
fonts = {}
offset_y = {}
def get_font(size: int) -> pygame.font.Font: # for internal use only
    if size not in fonts:
        fonts[size] = pygame.font.Font("../resources/font.ttf", size)
        offset_y[size] = fonts[size].metrics("f")[0][3] - fonts[size].get_ascent()
    return fonts[size]

# adapter for pygame.Surface
class Surface():
    @staticmethod
    def load(path: str):
        return Surface.copy(pygame.image.load(path))

    @staticmethod
    def copy(surface):
        if isinstance(surface, Surface):
            surface = surface.surface
        new = Surface()
        new.surface = surface
        return new

    @staticmethod
    def create(width: int, height: int):
        surface = Surface()
        surface.surface = pygame.Surface((width, height), pygame.HWACCEL | pygame.SRCALPHA)
        return surface

    @staticmethod
    def createScreen(width: int, height: int):
        pygame.init()
        surface = Surface()
        surface.surface = pygame.display.set_mode((width, height), pygame.SRCALPHA)
        return surface

    def blit(self, source, position: tuple, align: align.Align = align.Q) -> None: # blits either Surface or pygame.Surface, the latter one for internal use only
        if isinstance(source, Surface):
            source = source.surface
        self.surface.blit(source, align(position, source.get_size()))

    def fill(self, shape: shapes.ClosedShape, color: color.Color = None) -> None:
        shape.fill(self.surface, draw.BGC(color))

    def stroke(self, shape: shapes.Shape, color: color.Color = None) -> None:
        shape.stroke(self.surface, draw.FGC(color))

    def draw(self, shape: shapes.Shape, colors: tuple = (None, None)) -> None:
        shape.draw(self.surface, (draw.FGC(colors[0]), draw.BGC(colors[1])))

    def scale(self, width: int, height: int):
        return Surface.copy(pygame.transform.scale(self.surface, (width, height)))

    def setAlpha(self, alpha: int) -> None:
        self.surface.set_alpha(alpha)

def Text(text: str, color: color.Color = None, size: int = 7) -> pygame.Surface:
    surface = Surface.create(get_font(size).size(text)[0], size + 1)
    surface.blit(get_font(size).render(text, True, draw.FGC(color).convert()),(0, offset_y[size]))
    return surface

def quit() -> typing.NoReturn:
    pygame.quit()
    archive.save()
    sys.exit()
