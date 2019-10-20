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


def test_pressure_collector(monkeypatch):
    def mock_pressure():
        return 1013.345

    monkeypatch.setattr(collector.sense, 'get_pressure', mock_pressure)
    assert collector.get_pressure() == 1013.3
