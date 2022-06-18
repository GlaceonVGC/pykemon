class Align():
    # -1 for the leftmost (top) pixel
    # 0 for the one in the center
    # 1 for the one beyond the rightmost (bottom) one
    @staticmethod
    def single(align: int, position: int, size: int) -> int:
        return position if align == -1 else position - size // 2 if align == 0 else position - size

    def __init__(self, align_x, align_y):
        self.align = (align_x, align_y)
        
    def __call__(self, position: tuple, size: tuple) -> tuple:
        return tuple(Align.single(self.align[i], position[i], size[i]) for i in range(2))

# one-letter abbreviations are named after the left-most letters on the keyboard
Q = LEFT_TOP = Align(-1, -1)
A = LEFT_CENTER = Align(-1, 0)
Z = LEFT_BOTTOM = Align(-1, 1)
W = CENTER_TOP = Align(0, -1)
S = CENTER = Align(0, 0)
X = CENTER_BOTTOM = Align(0, 1)
E = RIGHT_TOP = Align(1, -1)
D = RIGHT_CENTER = Align(1, 0)
C = RIGHT_BOTTOM = Align(1, 1)
