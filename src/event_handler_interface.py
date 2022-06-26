class EventHandlerInterface():
    def click(self, position: tuple) -> None:
        pass
    
    def key(self, key: int) -> None:
        pass

    def endClick(self) -> None:
        pass
