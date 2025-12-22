from notifications.domain.entities.notification import Notification
from notifications.domain.entities.notification_status import NotificationStatus
from notifications.domain.interfaces.notifier import Notifier
from notifications.domain.repositories.notification_repository import NotificationRepository

class SendNotificationUseCase:
    def __init__(
            self, 
            notifiers: list[Notifier], 
            notification_repository: NotificationRepository
        ):
        self.notifiers = notifiers
        self.notification_repository = notification_repository

    def execute(self, recipient: str, message: str) -> Notification:
        
        notification = Notification(recipient=recipient, message=message)

        for notifier in self.notifiers:
            try:
                notifier.send_notification(recipient, message)
                notification.status = NotificationStatus.SENT
                break
            except Exception:
                continue
        else:
            notification.status = NotificationStatus.FAILED
        
        self.notification_repository.save_notification(notification)
        return notification
