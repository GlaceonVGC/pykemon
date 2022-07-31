import adapter
import archive
import painter
import shapes

class MapPainter(painter.Painter):
    def getKeys(self) -> dict:
        return {}

    def getColors(self) -> tuple:
        return archive.current.colors

    def paintUpper(self, upper: adapter.Surface) -> None:
        upper.draw(shapes.Rectangle(64, 48, 192, 144))

    def paintLower(self, lower: adapter.Surface) -> None:
        pass

    def clickLower(self) -> None:
        pass

    def endClick(self) -> None:
        pass
