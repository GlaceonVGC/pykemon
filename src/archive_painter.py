import adapter
import archive
import config
import language
import painter
import shapes
import toolkit
import linear_animation

current = 0
animation = linear_animation.new(lambda self: current)
def previous() -> None:
    global current
    if current > 0:
        current -= 1
        animation.reset(-config.ARCHIVE_ANIMATION_SPEED)

def next() -> None:
    global current
    if current < len(archive.archives) - 1:
        current += 1
        animation.reset(config.ARCHIVE_ANIMATION_SPEED)

def get_archive() -> archive.Archive:
    return archive.archives[current]

class ArchivePainter(painter.PainterInterface):
    def __init__(self) -> None:
        self.radius = 100

    def getKeys(self) -> dict:
        return {config.UP: painter.operation(next, toolkit.const(language.SHOW_NEXT), lambda: current < len(archive.archives) - 1),
                config.DOWN: painter.operation(previous, toolkit.const(language.SHOW_PREVIOUS), lambda: current > 0),
                config.SELECT: painter.operation(lambda: 0, toolkit.const(language.CONFIRM))} # TODO

    def getColors(self) -> tuple:
        return get_archive().colors

    def getX(self, y: int) -> int:
        return (self.radius ** 2 - (88 - y) ** 2) ** 0.5 - self.radius + 56

    def paintUpper(self, upper: adapter.Surface) -> None:
        upper.stroke(shapes.Ellipse(56 - self.radius * 2, 88 - self.radius, self.radius * 2))
        upper.draw(shapes.Ellipse(52, 84, 8))
        upper.draw(shapes.Rectangle(61, 72, 255, 102))
        upper.blit(adapter.Text(get_archive().name), (63, 74))
        upper.blit(adapter.Text(language.DATE % get_archive().date), (63, 83))
        upper.blit(adapter.Text(language.LOCATION % get_archive().location), (63, 92))
        # TODO: Badges' position: (9 * k + 92, 92)
        other = [(current - i, 73 - i * 9) for i in range(1, 9)]
        other.extend([(current + i, 94 + i * 9) for i in range(1, 9)])
        other = [(i, y + (current - animation.get()) * 9) for i, y in other]
        for i, y in other:
            if i >= 0 and i < len(archive.archives):
                x = self.getX(y + 4) + 5
                a = archive.archives[i]
                upper.draw(shapes.Ellipse(x - 9, y, 8), a.colors)
                upper.blit(adapter.Text(a.name, a.colors[0]), (x, y))

    def paintLower(self, lower: adapter.Surface) -> None:
        pass

    def clickLower(self, position: tuple) -> None:
        pass

    def endClick(self) -> None:
        pass
