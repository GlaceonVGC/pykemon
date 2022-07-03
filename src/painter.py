import adapter
import align
import color
import config
import draw
import language
import linear_animation
import shapes
import toolkit

expandHint = False
def get_top_bound() -> int:
    return 191 - 15 * len(list(filter(lambda k: keys[k].condition(), keys))) if expandHint else 176

animation = linear_animation.new(lambda self: get_top_bound())
def switch_hint() -> None:
    global expandHint
    expandHint = not expandHint
    animation.reset((-1 if expandHint else 1) * config.HINT_ANIMATION_SPEED)

def operation(call, text, condition=toolkit.const(True)) -> type:
    class Operation():
        def __len__(self) -> int:
            return adapter.get_font(1).size(self.text())[0]
    return type("AnonymousOperation", (Operation,), {
        "__call__": lambda self: call(),
        "text": lambda self: text(),
        "condition": lambda self: condition()})()

keys = {}

class PainterInterface(): # interface, getColors(), paintUpper(), paintLower(), getKeys() and clickLower() to be defined
    def paintHint(self, upper: adapter.Surface, hint: int, position: tuple, a: align.Align = align.Q) -> None:
        surface = adapter.Surface.create(16 + 4 * len(keys[hint]), 16)
        surface.fill(shapes.Ellipse(1, 1, 14), color.WHITE)
        surface.blit(adapter.Text(config.KEY_STR[hint], color.BLACK, 8), (8, 4), align.W)
        surface.blit(adapter.Text(keys[hint].text(), color.WHITE), (16, 4))
        upper.blit(surface, position, a)

    def paintMoreHints(self, upper: adapter.Surface) -> None:
        top = int(animation.get())
        upper.fill(shapes.Rectangle(0, top, 256, 176), color.BLACK)
        if expandHint:
            y = 161
            for key in reversed(keys.keys()):
                if key != config.Y and y >= top and keys[key].condition():
                    self.paintHint(upper, key, (0, y))
                    y -= 15

    def paintHints(self, upper: adapter.Surface) -> None:
        upper.fill(shapes.Rectangle(0, 176, 256, 192), color.BLACK)
        if expandHint:
            self.paintHint(upper, config.Y, (0, 176))
        else:
            x = 0
            for key in keys:
                if key != config.Y and keys[key].condition():
                    self.paintHint(upper, key, (x, 176))
                    x += 16 + 4 * len(keys[key])
            self.paintHint(upper, config.Y, (254, 176), align.E)

    def paint(self) -> tuple:
        upper = adapter.Surface.create(256, 192)
        lower = adapter.Surface.create(256, 192)
        temp = adapter.Surface.create(256, 192)
        upper.fill(shapes.Rectangle(0, 0, 256, 192), color.WHITE)
        lower.fill(shapes.Rectangle(0, 0, 256, 192), color.WHITE)
        draw.set_colors(*self.getColors())
        if animation.get() < get_top_bound() and animation.a <= 0 and get_top_bound() > animation.dest:
            animation.reset(config.HINT_ANIMATION_SPEED)
        if animation.get() > get_top_bound() and animation.a >= 0 and get_top_bound() < animation.dest:
            animation.reset(-config.HINT_ANIMATION_SPEED)
        self.paintUpper(upper)
        self.paintLower(lower)
        self.paintMoreHints(temp)
        temp.setAlpha(191)
        upper.blit(temp, (0, 0))
        self.paintHints(upper)
        return upper, lower

    def key(self, key: int) -> None:
        if key in keys:
            keys[key]()

def set_current(new: PainterInterface) -> None:
    global current, keys
    current = new
    keys = {config.Y: operation(switch_hint, lambda: language.HIDE_HINTS if expandHint else language.SHOW_HINTS)}
    keys.update(new.getKeys())
