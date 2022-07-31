import color

def sandbox(file: str) -> None:
    with open(file) as f:
        exec(f.read(), {}, {})

def const(value):
    return lambda: value

def bind(function, argument):
    return lambda: function(argument)

def mix(a: color.Color, b: color.Color, p: float = 0.5):
    alpha, pa, pb = (a.a + b.a) // 2, a.a * p, b.a * (1 - p)
    return color.RGBA(int((a.r * pa + b.r * pb) / alpha), int((a.g * pa + b.g * pb) / alpha), int((a.b * pa + b.b * pb) / alpha))
