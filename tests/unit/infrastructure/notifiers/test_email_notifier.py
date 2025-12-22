import pytest
import sys
from io import StringIO
from notifications.infrastructure.notifiers.email_notifier import EmailNotifier

def test_email_notifier_sends_notification():
    
    notifier = EmailNotifier()
    recipient = "test@example.com"
    message = "This is a test notification."
    
    try:
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output

        notifier.send_notification(recipient, message)

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        assert True  # If no exception is raised, the test passes
        assert f"Sending email to {recipient} with message: {message}" in output  # Verifica se a mensagem está no terminal
    except Exception as e:
        pytest.fail(f"send_notification raised an exception: {e}")
    
