import random
import adapter
import align
import archive_painter
import config
import color
import language
import painter
import shapes
import toolkit
import version

class TitlePainter(painter.Painter):
    def __init__(self) -> None:
        self.log = random.choice(version.VERSIONS[-1].log)
        self.current = len(version.VERSIONS) - 1
        self.isPressed = False

    def getKeys(self) -> dict:
        return {config.SELECT: painter.operation(
            toolkit.bind(painter.set_current, archive_painter.ArchivePainter()),
            toolkit.const(language.SELECT_ARCHIVE))}

    def setCurrent(self, newCurrent: int) -> None:
        self.current = version.get_proper(newCurrent)

    def getIndex(self) -> int:
        if adapter.mousePosition is None:
            self.isPressed = False
        if self.isPressed:
            self.setCurrent((adapter.mouseY - 61) * len(version.VERSIONS) // 118)
        return self.current

    def getVersion(self) -> version.Version:
        return version.VERSIONS[self.getIndex()]

    def getTop(self) -> int:
        return 61 + 118 * self.getIndex() // len(version.VERSIONS)

    def getBottom(self) -> int:
        return 64 + 118 * (self.getIndex() + 1) // len(version.VERSIONS)

    def getColors(self) -> tuple:
        return (color.BLACK, color.Gray(170))

    def paintUpper(self, upper: adapter.Surface) -> None:
        upper.blit(adapter.Surface.load("../resources/background.bmp"), (0, 0))
        upper.blit(adapter.Text(version.NAME, None, 71), (128, 1), align.W)
        upper.blit(adapter.Text(version.VERSIONS[-1].name), (2, 74))
        upper.blit(adapter.Text(self.log), (254, 74), align.E)
        upper.blit(adapter.Text(language.PRESS_SELECT_TO_CONTINUE), (128, 175), align.X)

    def paintLower(self, lower: adapter.Surface) -> None:
        lower.blit(adapter.Text(language.UPDATE_LOG, None, 48), (1, 1))
        lower.stroke(shapes.Line((1, 50), (254, 50)))
        lower.blit(adapter.Text(self.getVersion().name, None, 24), (1, 52))
        for i, j in enumerate(self.getVersion().log[:10]):
            lower.draw(shapes.Ellipse(1, 77 + 9 * i, 8))
            lower.blit(adapter.Text(j), (10, 77 + 9 * i))
        lower.draw(shapes.Polygon((249, 52), (254, 57), (243, 57), (248, 52)))
        lower.draw(shapes.Rectangle(243, 59, 255, 184))
        lower.draw(shapes.Rectangle(245, self.getTop(), 253, self.getBottom()),
                   (None, color.Gray(85)))
        lower.draw(shapes.Polygon((254, 185), (249, 190), (248, 190), (243, 185)))

    def clickLower(self, position: tuple) -> None:
        if position[1] <= 57 and position[0] + position[1] >= 300 and position[0] - position[1] <= 197:
            self.setCurrent(self.current - 1)
        elif position[1] >= 185 and position[0] + position[1] <= 439 and position[0] - position[1] >= 58:
            self.setCurrent(self.current + 1)
        elif position[0] >= 243 and position[0] <= 254:
            if position[1] >= 59 and position[1] < self.getTop():
                self.setCurrent(self.current - 1)
            elif position[1] > self.getBottom() and position[1] <= 183:
                self.setCurrent(self.current + 1)
            elif position[1] >= self.getTop() and position[1] <= self.getBottom():
                self.isPressed = True

    def endClick(self) -> None:
        self.isPressed = False
