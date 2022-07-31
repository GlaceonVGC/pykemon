import map_manager
import toolkit
class Map():
    def __init__(self, name, tiles: dict) -> None:
        self.name = name
        for tile in tiles.values():
            tile.map = self
        self.tiles = tiles

maps = []
toolkit.sandbox("maps.py")
for map in maps:
    map_manager.manager.tile.update(map)
