import event_handler_interface
import painters

class EventHandler(event_handler_interface.EventHandlerInterface):
    def click(self, position: tuple) -> None:
        painters.current.click(position)
    def key(self, key: int) -> None:
        painters.current.key(key)
