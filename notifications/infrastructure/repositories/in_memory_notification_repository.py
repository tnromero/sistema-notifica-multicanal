
from notifications.domain.entities.notification import Notification
from notifications.domain.repositories.notification_repository import NotificationRepository


class InMemoryNotificationRepository(NotificationRepository):
    def __init__(self):
        self.notifications = []

    def save_notification(self, notification: Notification) -> None:
        self.notifications.append(notification)

    def get_all(self) -> list[Notification]:
        return self.notifications