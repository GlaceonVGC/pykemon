NAME = "Pykemon"

class Version():
    def __init__(self, name: str, *log: tuple) -> int:
        self.name = name
        self.log = log

    def __len__(self) -> int:
        return len(self.log)

VERSIONS = (
    Version("DEV 0.0", "Date: Jul. 4 2022", "Completed title section", "Completed archive selection section"),
    Version("DEV 0.1", "Under Development", "TODO: Complete map section"),
)

def get_proper(index: int) -> int:
    return max(0, min(len(VERSIONS) - 1, index))
