import datetime
import pytest
from django.test import TestCase
from mixer.backend.django import mixer

from collector.models import Time, Temperature, Humidity

pytestmark=pytest.mark.django_db


def test_db_objects():
    time = mixer.blend('collector.Time')
    temp = mixer.blend('collector.Temperature', time=time)
    humidity = mixer.blend('collector.Humidity', time=time)
    assert time and temp and humidity
