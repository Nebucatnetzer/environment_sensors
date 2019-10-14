import datetime
import pytest
from django.test import TestCase

from collector.models import Time, Temperatur, Humidity

pytestmark=pytest.mark.django_db


def test_create_temperatur():
    time = Time.objects.create(value=datetime.datetime.now())
    temp = Temperatur.objects.create(value=20.0, time=time)
    assert False
