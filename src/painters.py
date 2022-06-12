import random
import adapter
import color
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
        self.information_x = 253 - len(self.information) * 6
    def paint(self) -> tuple:
        self.prepare()
        self.upper.fill(shapes.Rectangle(0, 0, 256, 192), color.Color.RGB(255, 255, 255))
        self.upper.fgcolor = color.Color.RGB(0, 0, 0)
        self.upper.write(version.NAME, (2, 2), None, 71)
        self.upper.write(version.VERSION, (2, 76))
        self.upper.write(self.information, (self.information_x, 76))
        self.upper.write("press select to continue", (56, 170))
        return self.upper, self.lower

current = TitlePainter()
