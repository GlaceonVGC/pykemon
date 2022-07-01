import adapter

class LinearAnimation(): # interface, getDestination() to be implemented
    def __init__(self) -> None:
        self.terminate()

    def get(self) -> int:
        return int(self.a * adapter.get_tick() + self.b)

    def reset(self, a: float) -> None:
        self.b -= (a - self.a) * adapter.get_tick()
        self.a = a
        self.dest = self.getDestination()

    def terminate(self) -> None:
        self.a = 0
        self.b = self.dest = self.getDestination()

def new(function) -> LinearAnimation:
    return type("Anonymous", (LinearAnimation,), {"getDestination": function})()