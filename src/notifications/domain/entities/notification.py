from dataclasses import dataclass

from notifications.domain.entities.notification_status import (
    NotificationStatus,
)


@dataclass
class Notification:
    recipient: str
    message: str
    status: NotificationStatus = NotificationStatus.PENDING
