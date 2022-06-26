import adapter
import archive
import color
import language
import painter
import shapes

class ArchivePainter(painter.PainterInterface):
    def __init__(self) -> None:
        super().__init__()
        self.radius = 100
        self.current = 0

    def getColors(self) -> tuple:
        return (color.BLACK, color.RGBA(170, 170, 170))

    def getX(self, y: int) -> int:
        return (self.radius ** 2 - (88 - y) ** 2) ** 0.5 - self.radius + 56

    def paintUpper(self, upper: adapter.Surface) -> None:
        upper.stroke(shapes.Ellipse(56 - self.radius * 2, 88 - self.radius, self.radius * 2))
        upper.draw(shapes.Ellipse(52, 84, 8))
        upper.draw(shapes.Rectangle(61, 72, 256, 30))
        upper.blit(adapter.Text("DEMO"), (63, 74))
        upper.blit(adapter.Text(language.PROGRESS % archive.archives[self.current].progress), (63, 83))
        upper.blit(adapter.Text(language.BADGE), (63, 92))
        # Badges' position: (9k+92, 92)
        for i, y in ((i, 64 - i * 9) for i in range(min(8, self.current))):
            x = self.getX(y + 4) + 5
            upper.draw(shapes.Ellipse(x - 9, y, 8))
            upper.blit(adapter.Text("DEMO"), (x, y))
        for i, y in ((i, 103 + i * 9) for i in range(min(8, len(archive.archives) - self.current - 1))):
            x = self.getX(y + 4) + 5
            upper.draw(shapes.Ellipse(x - 9, y, 8))
            upper.blit(adapter.Text("DEMO"), (x, y))

    def paintLower(self, lower: adapter.Surface) -> None:
        pass

    def clickLower(self, position: tuple) -> None:
        pass

    def endClick(self) -> None:
        pass
