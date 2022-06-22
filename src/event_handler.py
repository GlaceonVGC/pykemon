import event_handler_interface
import painter

class EventHandler(event_handler_interface.EventHandlerInterface):
    def click(self, position: tuple) -> None:
        if position[1] >= 192:
            painter.current.clickLower((position[0], position[1] - 192))
        
    def key(self, key: int) -> None:
        painter.current.key(key)
