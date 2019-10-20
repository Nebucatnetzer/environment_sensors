import datetime
import pytest
from django.test import TestCase
from mixer.backend.django import mixer

from collector import collector

pytestmark=pytest.mark.django_db


def test_temp_collector(monkeypatch):
    def mock_temp():
        return 25.345

    monkeypatch.setattr(collector.sense, 'get_temperature', mock_temp)
    assert collector.get_temperature() == 25.3
