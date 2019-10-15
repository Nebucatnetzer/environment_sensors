import datetime
import pytest
from django.test import TestCase
from mixer.backend.django import mixer

from collector import collector

pytestmark=pytest.mark.django_db


def test_collector():
    print(str(collector.get_temperature()))
