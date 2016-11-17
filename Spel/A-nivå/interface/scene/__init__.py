from abc import ABC, abstractmethod

class Scene(ABC):
    """Abstract class responsible of drawing to window."""

    def __init__(self, target):
        """Create an instance that renders to target."""

        self.target = target

    @abstractmethod
    def draw(self):
        """Called when the instance should render its content."""

        pass

    @abstractmethod
    def update(self, t):
        """Called when the instance should run update code.
        t is the duration of the main loop. An instance
        of the scene to switch to should be returned or
        None if the scene should not change."""

        pass

    @abstractmethod
    def event(self, events):
        """Called when SFML has caught an event. events is
        a list containing all caught events."""

        pass
