import adapter
import archive
import config
import language
import map_painter
import painter
import shapes
import toolkit
import linear_animation

bound = 0
animation = linear_animation.new(lambda self: bound)
def previous() -> None:
    global bound
    if bound > 0:
        bound -= 1
        if not create:
            archive.current = archive.archives[bound]
        animation.reset(-config.ARCHIVE_ANIMATION_SPEED)

def next() -> None:
    global bound
    if bound < len(archive.archives) - 1:
        bound += 1
        if not create:
            archive.current = archive.archives[bound]
        animation.reset(config.ARCHIVE_ANIMATION_SPEED)

def get_main() -> int:
    return int(animation.get() + 0.5)

def get_archive() -> archive.Archive:
    return archive.archives[get_main()]

create = False
def switch_create() -> None:
    global create
    create = not create
    archive.current = archive.new if create else archive.archives[bound]

def confirm() -> None:
    painter.append_painter(map_painter.MapPainter())
    if create:
        archive.archives.append(archive.new)

class ArchivePainter(painter.Painter):
    def __init__(self) -> None:
        self.radius = 100

    def getKeys(self) -> dict:
        return {config.UP: painter.operation(next, toolkit.const(language.SHOW_NEXT), lambda: bound < len(archive.archives) - 1),
                config.DOWN: painter.operation(previous, toolkit.const(language.SHOW_PREVIOUS), lambda: bound > 0),
                config.SELECT: painter.operation(confirm, toolkit.const(language.CONFIRM)),
                config.B: painter.operation(switch_create, lambda: language.SELECT_ARCHIVE if create else language.CREATE_ARCHIVE)}

    def getColors(self) -> tuple:
        return get_archive().colors

    def getX(self, y: int) -> int:
        return (self.radius ** 2 - (88 - y) ** 2) ** 0.5 - self.radius + 56

    def paintUpper(self, upper: adapter.Surface) -> None:
        offset = (get_main() - animation.get()) * 9
        upper.stroke(shapes.Ellipse(56 - self.radius * 2, 88 - self.radius, self.radius * 2))
        upper.draw(shapes.Ellipse(52, 84 + offset, 8))
        upper.draw(shapes.Rectangle(61, 72 + offset, 255, 102 + offset))
        upper.blit(adapter.Text(get_archive().name), (63, 74 + offset))
        upper.blit(adapter.Text(language.DATE % get_archive().date), (63, 83 + offset))
        upper.blit(adapter.Text(language.LOCATION % get_archive().location), (63, 92 + offset))
        other = [(-i, 73) for i in range(1, 9)][:get_main()]
        other.extend([(i, 94) for i in range(1, 9)][:len(archive.archives) - get_main() - 1])
        for i, y in [(get_main() + i, y + offset + i * 9) for i, y in other]:
            x = self.getX(y + 4) + 5
            a = archive.archives[i]
            upper.draw(shapes.Ellipse(x - 9, y, 8), a.colors)
            upper.blit(adapter.Text(a.name, a.colors[0]), (x, y))

    def paintLower(self, lower: adapter.Surface) -> None:
        # TODO there will be something to display
        lower.draw(shapes.Rectangle(7, 1, 87, 191), archive.current.colors)
        lower.draw(shapes.Rectangle(88, 1, 168, 191), archive.current.colors)
        lower.draw(shapes.Rectangle(169, 1, 249, 191), archive.current.colors)
        lower.draw(shapes.Polygon((5, 91), (5, 100), (1, 96), (1, 95)), archive.current.colors)
        lower.draw(shapes.Polygon((254, 96), (254, 95), (250, 91), (250, 100)), archive.current.colors)

    def clickLower(self) -> None:
        pass

    def endClick(self) -> None:
        pass
