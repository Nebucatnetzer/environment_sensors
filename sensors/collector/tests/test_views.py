import pytest
from mixer.backend.django import mixer

from django.test import Client

from .helper import in_content, not_in_content

pytestmark=pytest.mark.django_db


def test_index_temperature():
    response = Client().get('/')
    assert response.status_code == 200

