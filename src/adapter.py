import sys
import pygame
import align
import color
import config
import draw
import event_handler_interface
import shapes

# adapter for pygame.time.get_ticks
# varible ticks is to be changed in function new_frame,
# so that get_tick() would be the same within one frame
ticks = 0
def get_tick() -> int:
    return ticks

mousePosition = (0, 0)
def get_mouse_position() -> tuple:
    return mousePosition

# setting event handler
eventHandler = event_handler_interface.EventHandlerInterface() # a dull one for default
def set_event_handler(newHandler) -> None:
    global eventHandler
    eventHandler = newHandler

# displaying the screen, setting the time of the frame and reacting to events
keys = {}
def new_frame() -> None:
    global ticks, mousePosition
    pygame.display.flip()
    ticks = pygame.time.get_ticks()
    mousePosition = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key not in keys:
                keys[event.key] = get_tick()
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                del keys[event.key]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            eventHandler.click(get_mouse_position())
    for key in keys:
        while keys[key] <= get_tick():
            keys[key] += config.KEY_INTERVAL
            eventHandler.key(key)

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
        shape.draw(self.surface, (draw.BGC(colors[0]), draw.FGC(colors[1])))

    def scale(self, width: int, height: int):
        return Surface.copy(pygame.transform.scale(self.surface, (width, height)))

def Text(text: str, color: color.Color = None, size: int = 7) -> pygame.Surface:
    surface = Surface.create(get_font(size).size(text)[0], size + 1)
    surface.blit(get_font(size).render(text, True, draw.FGC(color).convert()), (0, offset_y[size]))
    return surface

def quit() -> None:
    pygame.quit()
