def sandbox(code: str) -> None:
    exec(code, {}, {})

def const(value):
    return lambda: value

def bind(function, argument):
    return lambda: function(argument)