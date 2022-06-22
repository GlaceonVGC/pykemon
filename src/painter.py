import adapter
import align
import color
import config
import draw
import language
import shapes

expandHint = False
hintAnimationTopA = 0
hintAnimationTopB = 176

def get_top() -> int:
    return int(hintAnimationTopA * adapter.get_tick() + hintAnimationTopB)

class Operation(): # interface, __call__() and text() to be defined
    def __len__(self) -> int:
        return adapter.get_font(1).size(self.text())[0]

class YOperation(Operation):
    def __call__(self) -> None:
        global hintAnimationTopA, hintAnimationTopB, expandHint
        hintAnimationTopB = get_top()
        expandHint = not expandHint
        hintAnimationTopA = (-1 if expandHint else 1) * config.HINT_ANIMATION_SPEED
        hintAnimationTopB -= hintAnimationTopA * adapter.get_tick()

    def text(self) -> str:
        return language.HIDE_HINTS if expandHint else language.SHOW_HINTS

class PainterInterface(): # interface, getColors(), paintUpper(), paintLower() and clickLower() to be defined
    def __init__(self) -> None:
        self.keys = {config.Y: YOperation()}

    def getHintAnimationTopBound(self) -> int:
        return 191 - 15 * len(self.keys) if expandHint else 176

    def paintHint(self, upper: adapter.Surface, hint: int, position: tuple, a: align.Align = align.Q) -> None:
        surface = adapter.Surface.create(16 + 4 * len(self.keys[hint]), 16)
        surface.fill(shapes.Ellipse(1, 1, 14), color.WHITE)
        surface.blit(adapter.Text(config.KEY_STR[hint], color.BLACK, 8),
                     (8, 4), align.W)
        surface.blit(adapter.Text(self.keys[hint].text(), color.WHITE), (16, 4))
        upper.blit(surface, position, a)

    def paintHints(self, upper: adapter.Surface) -> None:
        if (get_top() > self.getHintAnimationTopBound()) ^ expandHint:
            global hintAnimationTopA, hintAnimationTopB
            hintAnimationTopA = 0
            hintAnimationTopB = self.getHintAnimationTopBound()
        upper.fill(shapes.Rectangle(0, get_top(), 256, 176 - get_top()),
                   color.BLACK.alpha(191))
        upper.fill(shapes.Rectangle(0, 176, 256, 16), color.BLACK)
        if expandHint:
            y = 161
            for key in reversed(self.keys.keys()):
                if key in config.KEY_STR and key != config.Y and y >= get_top():
                    self.paintHint(upper, key, (0, y))
                    y -= 15
            self.paintHint(upper, config.Y, (0, 176))
        else:
            x = 0
            for key in self.keys:
                if key in config.KEY_STR and key != config.Y:
                    self.paintHint(upper, key, (x, 176))
                    x += 16 + 4 * len(self.keys[key])
            self.paintHint(upper, config.Y, (254, 176), align.E)

    def paint(self) -> tuple:
        upper = adapter.Surface.create(256, 192)
        lower = adapter.Surface.create(256, 192)
        upper.fill(shapes.Rectangle(0, 0, 256, 192), color.WHITE)
        lower.fill(shapes.Rectangle(0, 0, 256, 192), color.WHITE)
        draw.fgc, draw.bgc = self.getColors()
        self.paintUpper(upper)
        self.paintLower(lower)
        self.paintHints(upper)
        return upper, lower

    def key(self, key: int) -> None:
        if key in self.keys:
            self.keys[key]()
