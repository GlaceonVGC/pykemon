import language
class Archive():
    def __init__(self, name: str, progress: int) -> None:
        self.name = name
        self.progress = progress

    @staticmethod
    def new():
        return Archive(language.UNINITIALIZED_NAME, 0)

archives = []
with open("archives.py") as f:
    exec(f.read())
