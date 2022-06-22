import adapter
import painter

class ArchivePainter(painter.PainterInterface):
    def __init__(self) -> None:
        super().__init__()

    def paintUpper(self, upper: adapter.Surface) -> None:
        pass

    def paintLower(self, lower: adapter.Surface) -> None:
        pass

    def clickLower(self, position: tuple) -> None:
        pass
