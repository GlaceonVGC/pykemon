import tile

class MapManager():
    def __init__(self) -> None:
        self.tiles = {}

    def get(self, *position: tuple):
        return self.tiles[position] if position in self.tiles else tile.tiles["void"]()

manager = MapManager()
