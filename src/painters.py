import adapter
import color
import geometry

class PainterInterface():
    def prepare(self):
        self.upper = adapter.Surface.create(256, 192)
        self.lower = adapter.Surface.create(256, 192)
        
    def paint(self):
        self.prepare()
        return self.upper, self.lower
    
    def click(self, position: tuple) -> None:
        pass
    
    def key(self, key: int) -> None:
        pass

class TitlePainter(PainterInterface):
    def paint(self):
        self.prepare()
        self.upper.fill(geometry.Rectangle(0, 0, 256, 192), color.Color.RGB(255, 255, 255))
        return self.upper, self.lower

current = TitlePainter()
