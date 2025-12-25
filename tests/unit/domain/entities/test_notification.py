from notifications.domain.entities.notification import (
    Notification,
    NotificationStatus,
)


def test_notification_initialization():
    notification = Notification(
        recipient="test@example.com", message="Test Subject"
    )

    assert notification.recipient == "test@example.com"
    assert notification.message == "Test Subject"
    assert notification.status == NotificationStatus.PENDING
