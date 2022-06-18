import random
import pygame
import adapter
import align
import color
import config
import language
import shapes
import version

class PainterInterface():
    def y(self) -> None:
        if self.hintAnimationTopA == 0:
            if self.hintAnimationTopB == 176:
                self.hintAnimationTopA = -config.HINT_ANIMATION_SPEED
                self.hintAnimationTopB -= self.hintAnimationTopA * adapter.get_tick()
                self.hintAnimationTBound = adapter.get_tick() + 16 / config.HINT_ANIMATION_SPEED
            else:
                self.hintAnimationTopA = config.HINT_ANIMATION_SPEED
                self.hintAnimationTopB -= self.hintAnimationTopA * adapter.get_tick()
                self.hintAnimationTBound = adapter.get_tick() + 16 / config.HINT_ANIMATION_SPEED

    def __init__(self) -> None:
        self.keyReaction = {config.Y: self.y}
        self.hintAnimationTopA = 0
        self.hintAnimationTopB = 176
        self.hintAnimationTBound = 0

    def getTop(self) -> int:
        return int(self.hintAnimationTopA * adapter.get_tick() + self.hintAnimationTopB)

    def prepare(self) -> None:
        self.upper = adapter.Surface.create(256, 192)
        self.lower = adapter.Surface.create(256, 192)

    def paintHint(self, hint: tuple, position: tuple, a: align.Align) -> None:
        surface = adapter.Surface.create(16 + 4 * len(hint[1]), 16)
        surface.fill(shapes.Ellipse(1, 1, 14), color.WHITE)
        surface.blit(adapter.render(config.KEY_STR[hint[0]], color.BLACK, 8), (8, 4), align.W)
        surface.blit(adapter.render(hint[1], color.WHITE), (16, 4))
        self.upper.blit(surface, position, a)

    def paintHints(self, hints: dict) -> None:
        if adapter.get_tick() >= self.hintAnimationTBound:
            self.hintAnimationTopB += self.hintAnimationTopA * self.hintAnimationTBound
            self.hintAnimationTopA = 0
            self.hintAnimationTBound = adapter.get_tick()
        self.upper.fill(shapes.Rectangle(0, self.getTop(), 256, 176 - self.getTop()), color.BLACK.alpha(127))
        self.upper.fill(shapes.Rectangle(0, 176, 256, 16), color.BLACK)
        x = 0
        for key in hints:
            if key in config.KEY_STR and key != config.Y:
                self.paintHint((key, hints[key]), (x, 192), align.Z)
                x += 16 + 4 * len(hints[key])
        self.paintHint((config.Y, language.SHOW_HINTS), (254, 192), align.C)

    def paint(self) -> tuple:
        self.prepare()
        return self.upper, self.lower

    def click(self, position: tuple) -> None:
        pass # the default situation

    def key(self, key: int) -> None:
        if key in self.keyReaction:
            self.keyReaction[key]()
        pass # the default situation

class TitlePainter(PainterInterface):
    def select(self) -> None:
        global painter
        painter = ArchivePainter()

    def __init__(self) -> None:
        super().__init__()
        self.keyReaction[config.SELECT] = self.select
        self.information = random.choice(version.INFORMATION)

    def paint(self) -> tuple:
        self.prepare()
        self.upper.fill(shapes.Rectangle(0, 0, 256, 192), color.WHITE)
        self.upper.fgcolor = color.BLACK
        self.upper.blit(adapter.render(version.NAME, None, 71), (128, 1), align.W)
        self.upper.blit(adapter.render(version.VERSION), (2, 74))
        self.upper.blit(adapter.render(self.information), (254, 74), align.E)
        self.upper.blit(adapter.render(language.PRESS_SELECT_TO_CONTINUE), (128, 175), align.X)
        self.paintHints({config.SELECT: language.SELECT_ARCHIVE})
        self.lower.fill(shapes.Rectangle(0, 0, 256, 192), color.WHITE)
        return self.upper, self.lower

current = TitlePainter()
