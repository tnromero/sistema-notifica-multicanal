from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send_notification(self, recipient: str, message: str) -> None:
        """Send a notification to the specified recipient with the given message."""
        pass