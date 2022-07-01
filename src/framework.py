import pygame
import adapter
import config
import painter

def map_to_lower(position: tuple) -> tuple:
    return (position[0], position[1] - 192) if position[1] >= 192 else None

keys = {}
click = None
def new_frame() -> None:
    global click, mouseX, mouseY
    pygame.display.flip()
    adapter.ticks = pygame.time.get_ticks()
    adapter.mousePosition = map_to_lower(pygame.mouse.get_pos())
    if adapter.mousePosition is not None:
        mouseX, mouseY = adapter.mousePosition
    else:
        mouseX = mouseY = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            adapter.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key not in keys:
                keys[event.key] = adapter.get_tick()
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                del keys[event.key]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if adapter.mousePosition is not None and click is None:
                painter.current.clickLower(adapter.mousePosition)
                click = adapter.mousePosition
        elif event.type == pygame.MOUSEBUTTONUP:
            if click is not None:
                painter.current.endClick()
                click = None
    for key in keys:
        while keys[key] <= adapter.get_tick():
            keys[key] += config.KEY_INTERVAL
            painter.current.key(key)
