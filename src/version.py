NAME = "Pykemon"

class Version():
    def __init__(self, name: str, *log: tuple) -> int:
        self.name = name
        self.log = log

    def __len__(self) -> int:
        return len(self.log)

VERSIONS = (
    Version("some version #1", "some feature #1", "some feature #2", "some feature #3"),
    Version("some version #2", "some feature #4"),
    Version("DEV 0.0", "Date: Jun. 22 2022", "Added \"Update Log\" section"),
)
