import sys
import pygame
import color
import config
import event_handler_interface

# adapter for pygame.time.get_ticks
# varible ticks is to be changed in function new_frame,
# so that get_tick() would be the same within one frame
ticks = 0
def get_tick() -> int:
    return ticks

# setting event handler
eventHandler = event_handler_interface.EventHandlerInterface() # a dull one for default
def set_event_handler(newHandler) -> None:
    global eventHandler
    eventHandler = newHandler

# displaying the screen, setting the time of the frame and reacting to events
keys = {}
def new_frame() -> None:
    global ticks
    pygame.display.flip()
    ticks = pygame.time.get_ticks()
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
            eventHandler.click(pygame.mouse.get_pos())
    for key in keys:
        while keys[key] <= get_tick():
            keys[key] += config.KEY_INTERVAL
            eventHandler.key(key)

# adapter for pygame.Surface
class Surface():
    @staticmethod
    def create(width: int, height: int):
        surface = Surface()
        surface.surface = pygame.Surface((width, height), pygame.HWACCEL | pygame.SRCALPHA)
        return surface

    @staticmethod
    def createScreen(width: int, height: int):
        pygame.init()
        surface = Surface()
        surface.surface = pygame.display.set_mode((width, height))
        return surface

    def blit(self, source, position: tuple) -> None:
        self.surface.blit(source.surface, position)

    def fill(self, shape, color: color.Color = None) -> None:
        shape.fill(self.surface, self.backgroundColor if color is None else color)
