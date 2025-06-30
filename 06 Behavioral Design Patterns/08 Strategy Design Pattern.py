from abc import ABC, abstractmethod


# ----------- STRATEGY INTERFACE -----------
class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start: str, end: str) -> None:
        ...


# ----------- CONCRETE STRATEGIES -----------
class DrivingStrategy(RouteStrategy):
    def build_route(self, start: str, end: str) -> None:
        print(f"🚗 Calculating driving route from {start} to {end} via highways and roads.")


class WalkingStrategy(RouteStrategy):
    def build_route(self, start: str, end: str) -> None:
        print(f"🚶 Calculating walking route from {start} to {end} via pedestrian paths.")


class PublicTransportStrategy(RouteStrategy):
    def build_route(self, start: str, end: str) -> None:
        print(f"🚌 Calculating public transport route from {start} to {end} using bus/train schedules.")


# ----------- CONTEXT -----------
class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy
        print(f"[Navigator] Strategy changed to: {strategy.__class__.__name__}")

    def navigate(self, start: str, end: str) -> None:
        print(f"[Navigator] Routing from {start} to {end}...")
        self._strategy.build_route(start, end)


# ----------- CLIENT CODE -----------
def main():
    # Create context with a default strategy
    navigator = Navigator(DrivingStrategy())

    # Simulate user selecting different modes
    navigator.navigate("Central Park", "Empire State Building")

    navigator.set_strategy(WalkingStrategy())
    navigator.navigate("Central Park", "Empire State Building")

    navigator.set_strategy(PublicTransportStrategy())
    navigator.navigate("Central Park", "Empire State Building")


if __name__ == "__main__":
    main()
