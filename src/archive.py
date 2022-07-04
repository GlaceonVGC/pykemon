import color
import date
import language
import location
import toolkit
class Archive():
    def __init__(self, name: str, colors: tuple, d: date.Date, l: location.Location) -> None:
        self.name = name
        self.colors = colors
        self.date = d
        self.location = l

    def __repr__(self) -> str:
        return f"archive.Archive({self.name!r}, ({self.colors[0]!r}, {self.colors[1]!r}), {self.date!r}, {self.location!r})"

archives = []
new = Archive(language.UNINITIALIZED_NAME, (color.BLACK, color.Gray(170)), date.Date(), location.Location())
with open("archives.py") as f:
    toolkit.sandbox(f.read())
current = archives[0]

def save() -> None:
    with open("archives.py", "w") as f:
        f.write("import archive, color, date, location\n")
        for i in archives:
            f.write(f"archive.archives.append({i!r})\n")
