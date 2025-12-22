from notifications.domain.interfaces.notifier import Notifier


class EmailNotifier(Notifier):
    def send_notification(self, recipient: str, message: str) -> None:
        # Logic to send an email notification
        print(f"Sending email to {recipient} with message: {message}")