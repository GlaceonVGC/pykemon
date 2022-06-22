import random
import adapter
import align
import archive_painter
import config
import color
import language
import painter
import shapes
import version

class SelectOperation(painter.Operation):
    def __call__(self) -> None:
        painter.current = archive_painter.ArchivePainter()

    def text(self) -> str:
        return language.SELECT_ARCHIVE
    
class TitlePainter(painter.PainterInterface):
    def __init__(self) -> None:
        super().__init__()
        self.log = random.choice(version.VERSIONS[-1].log)
        self.keys[config.SELECT] = SelectOperation()
        self.current = len(version.VERSIONS) - 1

    def getTop(self, relation: int = None) -> int:
        return 118 * (self.current + relation) // len(version.VERSIONS)

    def getColors(self) -> tuple:
        return (color.BLACK, color.RGBA(170, 170, 170))

    def paintUpper(self, upper: adapter.Surface) -> None:
        upper.blit(adapter.Surface.load("../resources/background.bmp"), (0, 0))
        upper.blit(adapter.Text(version.NAME, None, 71), (128, 1), align.W)
        upper.blit(adapter.Text(version.VERSIONS[-1].name), (2, 74))
        upper.blit(adapter.Text(self.log), (254, 74), align.E)
        upper.blit(adapter.Text(language.PRESS_SELECT_TO_CONTINUE), (128, 175), align.X)

    def paintLower(self, lower: adapter.Surface) -> None:
        lower.blit(adapter.Text(language.UPDATE_LOG, None, 48), (1, 1))
        lower.stroke(shapes.Line((1, 50), (254, 50)))
        lower.blit(adapter.Text(version.VERSIONS[-1].name, None, 24), (1, 52))
        for i, j in enumerate(version.VERSIONS[self.current].log[:10]):
            lower.draw(shapes.Ellipse(1, 77 + 9 * i, 8))
            lower.blit(adapter.Text(j), (10, 77 + 9 * i))
        lower.draw(shapes.Polygon((249, 52), (254, 57), (243, 57), (248, 52)))
        lower.draw(shapes.Rectangle(243, 59, 12, 125))
        lower.draw(shapes.Rectangle(245, 61 + self.getTop(0),
                                    8, 3 + self.getTop(1) - self.getTop(0)),
                   (color.RGBA(85, 85, 85), None))
        lower.draw(shapes.Polygon((254, 185), (249, 190), (248, 190), (243, 185)))

    def toPrevious(self) -> None:
        self.current = max(0, self.current - 1)

    def toNext(self) -> None:
        self.current = min(len(version.VERSIONS) - 1, self.current + 1)

    def clickLower(self, position: tuple) -> None:
        if position[1] <= 57 and position[0] + position[1] >= 300 and position[0] - position[1] <= 197:
            self.toPrevious()
        elif position[1] >= 185 and position[0] + position[1] <= 439 and position[0] - position[1] >= 58:
            self.toNext()
        elif position[0] >= 243 and position[0] <= 254:
            if position[1] >= 59 and position[1] <= 60 + self.getTop(0):
                self.toPrevious()
            elif position[1] >= 65 + self.getTop(1) and position[1] <= 183:
                self.toNext()
            elif position[1] >= 61 + self.getTop(0) and position[1] <= 64 + self.getTop(1):
                pass
