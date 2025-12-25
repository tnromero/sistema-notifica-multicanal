from unittest.mock import Mock

import pytest


@pytest.fixture
def primary_notifier():
    return Mock()


@pytest.fixture
def fallback_notifier():
    return Mock()


@pytest.fixture
def notification_repository():
    return Mock()
