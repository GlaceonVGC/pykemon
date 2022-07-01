from adapter import *
from align import *
from color import *
from config import *
import draw
from language import *
import linear_animation
from shapes import *

expandHint = False
def get_top_bound() -> int:
    return 191 - 15 * len(keys) if expandHint else 176

animation = linear_animation.new(lambda self: get_top_bound())

class Operation(): # interface, __call__() and text() to be defined
    def __len__(self) -> int:
        return get_font(1).size(self.text())[0]

class YOperation(Operation):
    def __call__(self) -> None:
        global expandHint
        expandHint = not expandHint
        animation.reset((-1 if expandHint else 1) * HINT_ANIMATION_SPEED)
        
    def text(self) -> str:
        return HIDE_HINTS if expandHint else SHOW_HINTS

class PainterInterface(): # interface, getColors(), paintUpper(), paintLower() and clickLower() to be defined
    def __init__(self) -> None:
        global keys
        keys = {Y: YOperation()}

    def paintHint(self, upper: Surface, hint: int, position: tuple, a: Align = Q) -> None:
        surface = Surface.create(16 + 4 * len(keys[hint]), 16)
        surface.fill(Ellipse(1, 1, 14), WHITE)
        surface.blit(Text(KEY_STR[hint], BLACK, 8), (8, 4), W)
        surface.blit(Text(keys[hint].text(), WHITE), (16, 4))
        upper.blit(surface, position, a)

    def paintHints(self, upper: Surface) -> None:
        if animation.get() < get_top_bound() and animation.a < 0:
            if get_top_bound() <= animation.dest:
                animation.terminate()
            else:
                animation.reset(HINT_ANIMATION_SPEED)
        if animation.get() > 176 and animation.a > 0:
            animation.terminate()
        top = animation.get()
        upper.fill(Rectangle(0, top, 256, 176 - top), BLACK.alpha(191))
        upper.fill(Rectangle(0, 176, 256, 16), BLACK)
        if expandHint:
            y = 161
            for key in reversed(keys.keys()):
                if key in KEY_STR and key != Y and y >= top:
                    self.paintHint(upper, key, (0, y))
                    y -= 15
            self.paintHint(upper, Y, (0, 176))
        else:
            x = 0
            for key in keys:
                if key in KEY_STR and key != Y:
                    self.paintHint(upper, key, (x, 176))
                    x += 16 + 4 * len(keys[key])
            self.paintHint(upper, Y, (254, 176), E)

    def paint(self) -> tuple:
        upper = Surface.create(256, 192)
        lower = Surface.create(256, 192)
        upper.fill(Rectangle(0, 0, 256, 192), WHITE)
        lower.fill(Rectangle(0, 0, 256, 192), WHITE)
        draw.set_colors(*self.getColors())
        self.paintUpper(upper)
        self.paintLower(lower)
        self.paintHints(upper)
        return upper, lower

    def key(self, key: int) -> None:
        if key in keys:
            keys[key]()
