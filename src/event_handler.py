import event_handler_interface
import painter

class EventHandler(event_handler_interface.EventHandlerInterface):
    def click(self, position: tuple) -> None:
        painter.current.clickLower(position)
        
    def key(self, key: int) -> None:
        painter.current.key(key)

    def endClick(self) -> None:
        painter.current.endClick()
