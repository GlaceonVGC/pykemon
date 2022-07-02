import color
import language
class Archive():
    def __init__(self, name: str, progress: int, colors: tuple) -> None:
        self.name = name
        self.progress = progress
        self.colors = colors

    @staticmethod
    def new():
        return Archive(language.UNINITIALIZED_NAME, 0, (color.Gray(170), color.BLACK))

    def __str__(self) -> str:
        return f"Archive('{self.name}', {self.progress}, ({self.colors[0]}, {self.colors[1]}))"

archives = []
with open("archives.py") as f:
    exec(f.read())
