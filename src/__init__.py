import adapter
import framework
import title_painter
import painter

if __name__ == "__main__":
    painter.append_painter(title_painter.TitlePainter())
    screen = adapter.Surface.createScreen(256, 384)
    while True:
        screens = painter.painters[-1].paint()
        screen.blit(screens[0], (0, 0))
        screen.blit(screens[1], (0, 192))
        framework.new_frame()
