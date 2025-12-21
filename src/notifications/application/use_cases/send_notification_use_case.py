from notifications.domain.entities.notification import Notification
from notifications.domain.entities.notification_status import NotificationStatus
from notifications.domain.interfaces.notifier import Notifier
from notifications.domain.repositories.notification_repository import NotificationRepository

class SendNotificationUseCase:
    def __init__(
            self, 
            primary_notifier: Notifier, 
            fallback_notifier: Notifier,
            notification_repository: NotificationRepository
        ):
        self.primary_notifier = primary_notifier
        self.fallback_notifier = fallback_notifier
        self.notification_repository = notification_repository

    def execute(self, recipient: str, message: str) -> Notification:
        
        notification = Notification(recipient=recipient, message=message)

        try:
            self.primary_notifier.send_notification(recipient, message)
            notification.status = NotificationStatus.SENT
        
        except Exception:
            try:
                self.fallback_notifier.send_notification(recipient, message)
                notification.status = NotificationStatus.SENT
            except Exception:
                notification.status = NotificationStatus.FAILED
        
        self.notification_repository.save_notification(notification)
        return notification
