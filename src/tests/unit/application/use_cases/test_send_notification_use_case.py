import pytest

from notifications.application.use_cases.send_notification_use_case import SendNotificationUseCase
from notifications.domain.entities.notification_status import NotificationStatus

def test_send_notification_use_case_success_primary(primary_notifier, fallback_notifier, notification_repository):

    use_case = SendNotificationUseCase(
        primary_notifier=primary_notifier,
        fallback_notifier=fallback_notifier,
        notification_repository=notification_repository
    )

    result = use_case.execute(recipient="user@email.com", message="Test Message")
    assert result.status == NotificationStatus.SENT
    primary_notifier.send_notification.assert_called_once_with("user@email.com", "Test Message")
    fallback_notifier.send_notification.assert_not_called()
    notification_repository.save_notification.assert_called_once_with(result)

def test_send_notification_use_case_success_fallback(primary_notifier, fallback_notifier, notification_repository):
    primary_notifier.send_notification.side_effect = Exception("Primary notifier failed - email not sent")

    use_case = SendNotificationUseCase(
        primary_notifier=primary_notifier,
        fallback_notifier=fallback_notifier,
        notification_repository=notification_repository
    )

    result = use_case.execute(recipient="user@email.com", message="Test Message")
    assert result.status == NotificationStatus.SENT
    primary_notifier.send_notification.assert_called_once_with("user@email.com", "Test Message")
    fallback_notifier.send_notification.assert_called_once_with("user@email.com", "Test Message")
    notification_repository.save_notification.assert_called_once_with(result)

def test_send_notification_use_case_failure_both(primary_notifier, fallback_notifier, notification_repository):
    primary_notifier.send_notification.side_effect = Exception("Primary notifier failed - email not sent")
    fallback_notifier.send_notification.side_effect = Exception("Fallback notifier failed - SMS not sent")

    use_case = SendNotificationUseCase(
        primary_notifier=primary_notifier,
        fallback_notifier=fallback_notifier,
        notification_repository=notification_repository
    )

    result = use_case.execute(recipient="user@email.com", message="Test Message")
    assert result.status == NotificationStatus.FAILED
    primary_notifier.send_notification.assert_called_once_with("user@email.com", "Test Message")
    fallback_notifier.send_notification.assert_called_once_with("user@email.com", "Test Message")
    notification_repository.save_notification.assert_called_once_with(result)