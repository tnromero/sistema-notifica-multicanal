from notifications.infrastructure.repositories.in_memory_notification_repository import InMemoryNotificationRepository
from notifications.domain.entities.notification import Notification

def test_save_and_get_all_notification():
    repository = InMemoryNotificationRepository()
    
    notification_01 = Notification(recipient="test@example.com", message="Test notification")
    repository.save_notification(notification_01)

    notification_02 = Notification(recipient="+1234567890", message="Test notification")
    repository.save_notification(notification_02)
    notifications = repository.get_all_notifications()
    assert notifications == [notification_01, notification_02]