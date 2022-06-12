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
        self.information_x = 253 - len(self.information) * 4
    def paint(self) -> tuple:
        self.prepare()
        self.upper.fill(shapes.Rectangle(0, 0, 256, 192), color.Color.RGB(255, 255, 255))
        self.upper.write(version.NAME, (8, 2), color.Color.RGB(0, 0, 0), 32)
        self.upper.write(version.VERSION, (8, 36), color.Color.RGB(0, 0, 0), 16)
        self.upper.write(self.information, (self.information_x, 36), color.Color.RGB(0, 0, 0))
        return self.upper, self.lower

current = TitlePainter()
