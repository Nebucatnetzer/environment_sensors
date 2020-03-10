import pytest
from mixer.backend.django import mixer
from django.utils import timezone

from collector.models import Temperature, Humidity

pytestmark=pytest.mark.django_db


def test_db_objects():
    time = timezone.now()
    temp = mixer.blend('collector.Temperature', time=time)
    humidity = mixer.blend('collector.Humidity', time=time)
    assert time and temp and humidity
