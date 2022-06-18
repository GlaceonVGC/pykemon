import random
import adapter
import align
import color
import language
import shapes
import version

class PainterInterface():
    def prepare(self) -> None:
        self.upper = adapter.Surface.create(256, 192)
        self.lower = adapter.Surface.create(256, 192)
        
    def paint(self) -> tuple:
        self.prepare()
        return self.upper, self.lower
    
    def click(self, position: tuple) -> None:
        pass
    
    def key(self, key: int) -> None:
        pass

class TitlePainter(PainterInterface):
    def __init__(self):
        self.information = random.choice(version.INFORMATION)
    def paint(self) -> tuple:
        self.prepare()
        self.upper.fill(shapes.Rectangle(0, 0, 256, 192), color.WHITE)
        self.upper.fgcolor = color.BLACK
        self.upper.write(version.NAME, align.W((128, 1), (252, 72)), None, 71)
        self.upper.write(version.VERSION, align.Q((2, 74), (4 * len(version.VERSION), 8)))
        self.upper.write(self.information, align.E((254, 74), (4 * len(self.information), 8)))
        self.upper.write(language.PRESS_SELECT_TO_CONTINUE, align.X((128, 175), (4 * len(language.PRESS_SELECT_TO_CONTINUE), 8)))
        return self.upper, self.lower

current = TitlePainter()
