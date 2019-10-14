import pytest
from django.test import TestCase


pytestmark=pytest.mark.django_db


def test_create_temperatur():
    time = models.Time.create(value=datetime.datetime.now)
    temp = models.Temperatur.create(value=20.0, time=time)
    assert False
