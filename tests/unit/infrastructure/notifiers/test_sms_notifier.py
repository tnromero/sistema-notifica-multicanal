import sys
from io import StringIO

import pytest
from notifications.infrastructure.notifiers.sms_notifier import SMSNotifier


def test_sms_notifier_sends_notification():
    notifier = SMSNotifier()
    recipient = "+55511999999999"
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
        assert (
            f"Sending SMS to {recipient} with message: {message}" in output
        )  # Verifica se a mensagem está no terminal
    except Exception as e:
        pytest.fail(f"send_notification raised an exception: {e}")
