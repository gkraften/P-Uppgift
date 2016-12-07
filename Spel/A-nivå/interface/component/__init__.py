from abc import ABC, abstractmethod

class Component(ABC):
    """Abstract base class that all components such as
    buttons should inherit from."""

    def __init__(self, target):
        self.target = target

    @abstractmethod
    def draw(self):
        """Method that is called when the component
        should render itself."""

        pass

    def update(self, t):
        """Method called when component is allowed
        to update itself. t is the duration of the
        main loop."""

        pass

    def event(self, e):
        """Method called when an event has occurred.
        e is a list of all events that ocurred."""

        pass