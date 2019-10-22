import pytest

from collector import collector
from collector.models import Temperature, Humidity, Pressure

pytestmark=pytest.mark.django_db


def test_temp_collector(monkeypatch):
    def mock_temp():
        return 25.345

    monkeypatch.setattr(collector.sense, 'get_temperature', mock_temp)
    assert collector.get_temperature() == 25.5


def test_humidity_collector(monkeypatch):
    def mock_humidity():
        return 45.2356

    monkeypatch.setattr(collector.sense, 'get_humidity', mock_humidity)
    assert collector.get_humidity() == 45


def test_pressure_collector(monkeypatch):
    def mock_pressure():
        return 1013.345

    monkeypatch.setattr(collector.sense, 'get_pressure', mock_pressure)
    assert collector.get_pressure() == 1013


def test_values_to_db(monkeypatch):
    def mock_temp():
        return 25.345

    monkeypatch.setattr(collector.sense, 'get_temperature', mock_temp)

    def mock_humidity():
        return 45.2356

    monkeypatch.setattr(collector.sense, 'get_humidity', mock_humidity)

    def mock_pressure():
        return 1013.345

    monkeypatch.setattr(collector.sense, 'get_pressure', mock_pressure)
    collector.values_to_db()
    temp = Temperature.objects.get(pk=1)
    humidity = Humidity.objects.get(pk=1)
    pressure = Pressure.objects.get(pk=1)
    assert (temp.value == 25.5
            and humidity.value == 45
            and pressure.value == 1013)
