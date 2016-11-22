from abc import ABC, abstractmethod

class Component(ABC):
    """Abstract base class that all components such as
    buttons should inherit from."""

    @abstractmethod
    def draw(self, target):
        """Method that is called when the component
        should render itself. Target si what to render
        to."""

        pass

    def update(self):
        """Method called when component is allowed
        to update itself."""

        pass

    def event(self, e):
        """Method called when an event has occurred.
        e is a list of all events that ocurred."""

        pass