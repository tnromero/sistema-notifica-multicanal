from notifications.application.use_cases.send_notification_use_case import (
    SendNotificationUseCase,
)
from notifications.domain.entities.notification import Notification
from notifications.domain.interfaces.notifier import Notifier
from notifications.domain.repositories.notification_repository import (
    NotificationRepository,
)
from notifications.infrastructure.notifiers.email_notifier import EmailNotifier
from notifications.infrastructure.notifiers.sms_notifier import SMSNotifier
from notifications.infrastructure.repositories.in_memory_notification_repository import (
    InMemoryNotificationRepository,
)

email_notifier: Notifier = EmailNotifier()
sms_notifier: Notifier = SMSNotifier()
notification_repository: NotificationRepository = (
    InMemoryNotificationRepository()
)

use_case_send_notification = SendNotificationUseCase(
    notifiers=[email_notifier, sms_notifier],
    notification_repository=notification_repository,
)

notification: Notification = use_case_send_notification.execute(
    recipient="user@example.com", message="Hello, World!"
)

print(f"Notification sent with status: {notification.status}")
