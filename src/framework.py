import pygame
import adapter
import config
import painter

def map_to_lower(position: tuple) -> tuple:
    return (position[0], position[1] - 192) if position[1] >= 192 else (None, None)

time = {key: -config.KEY_INTERVAL for key in config.keys}
keys = set()
click = False
def new_frame() -> None:
    global click
    pygame.display.flip()
    adapter.ticks = pygame.time.get_ticks()
    adapter.mouseX, adapter.mouseY = map_to_lower(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            adapter.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key in config.keys and time[event.key] <= adapter.get_tick():
                time[event.key] = adapter.get_tick()
                keys.add(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys.remove(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (adapter.mouseX, adapter.mouseY) != (None, None):
                painter.painters[-1].clickLower()
                click = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if click:
                painter.painters[-1].endClick()
                click = False
    for key in keys:
        while time[key] <= adapter.get_tick():
            time[key] += config.KEY_INTERVAL
            painter.painters[-1].key(key)
