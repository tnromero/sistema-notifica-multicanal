from abc import ABC, abstractmethod

from notifications.domain.entities.notification import Notification

class NotificationRepository(ABC):
    
    @abstractmethod
    def save_notification(self, notification: Notification) -> None:
        """Save the notification details to the repository."""
        pass