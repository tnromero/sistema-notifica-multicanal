from notifications.domain.interfaces.notifier import Notifier


class SMSNotifier(Notifier):
    def send_notification(self, recipient: str, message: str) -> None:
        # Logic to send an SMS notification
        print(f"Sending SMS to {recipient} with message: {message}")
