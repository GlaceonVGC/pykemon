import toolkit
def new(identifier: str, **keys: dict) -> type:
    class Tile():
        def setHeight(self, height: int) -> None:
            self.height = height

    keys.setdefault("texture", "../resources/tiles/%s" % identifier)
    keys.setdefault("__init__", lambda self, height: self.setHeight(height))
    return type("AnonymousTile", (Tile,), keys)

identifiers = ["void", "grass"]
tiles = {identifier: new(identifier, __init__=lambda self: self.setHeight(0)) for identifier in identifiers}
