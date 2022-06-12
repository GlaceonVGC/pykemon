import adapter
import event_handler
import painters

if __name__ == "__main__":
    screen = adapter.Surface.createScreen(256, 384)
    adapter.set_event_handler(event_handler.EventHandler())
    while True:
        screens = painters.current.paint()
        screen.blit(screens[0], (0, 0))
        screen.blit(screens[1], (0, 192))
        adapter.new_frame()
