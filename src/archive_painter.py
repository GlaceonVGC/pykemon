import adapter
import archive
import config
import language
import painter
import shapes

UpOperation = painter.operation(
    __call__=lambda self: 0, # TODO
    text=lambda self: language.SHOW_PREVIOUS_ARCHIVE)

class ArchivePainter(painter.PainterInterface):
    def __init__(self) -> None:
        super().__init__()
        painter.keys[config.UP] = UpOperation()
        self.radius = 100
        self.current = 0

    @property
    def archive(self) -> archive.Archive:
        return archive.archives[self.current]

    def getColors(self) -> tuple:
        return self.archive.colors

    def getX(self, y: int) -> int:
        return (self.radius ** 2 - (88 - y) ** 2) ** 0.5 - self.radius + 56

    def paintUpper(self, upper: adapter.Surface) -> None:
        upper.stroke(shapes.Ellipse(56 - self.radius * 2, 88 - self.radius, self.radius * 2))
        upper.draw(shapes.Ellipse(52, 84, 8))
        upper.draw(shapes.Rectangle(61, 72, 255, 102))
        upper.blit(adapter.Text("DEMO"), (63, 74))
        upper.blit(adapter.Text(language.PROGRESS % self.archive.progress), (63, 83))
        upper.blit(adapter.Text(language.BADGE), (63, 92))
        # TODO: Badges' position: (9 * k + 92, 92)
        other = [(-i, 73 - i * 9) for i in range(1, 9)]
        other.extend([(i, 94 + i * 9) for i in range(1, 9)])
        for i, y in other:
            if i >= 0 and i < len(archive.archives):
                x = self.getX(y + 4) + 5
                a = archive.archives[self.current + i]
                upper.draw(shapes.Ellipse(x - 9, y, 8), a.colors)
                upper.blit(adapter.Text(a.name, a.colors[0]), (x, y))

    def paintLower(self, lower: adapter.Surface) -> None:
        pass

    def clickLower(self, position: tuple) -> None:
        pass

    def endClick(self) -> None:
        pass
