import adapter
import event_handler
import title_painter
import painter

if __name__ == "__main__":
    painter.current = title_painter.TitlePainter()
    screen = adapter.Surface.createScreen(256, 384)
    adapter.set_event_handler(event_handler.EventHandler())
    while True:
        screens = painter.current.paint()
        screen.blit(screens[0], (0, 0))
        screen.blit(screens[1], (0, 192))
        adapter.new_frame()
    adapter.quit()
