import os
from django.utils import timezone

if os.uname()[4].startswith("arm"):
    from sense_hat import SenseHat
else:
    from sense_emu import SenseHat

from .models import Time, Temperature, Humidity, Pressure

sense = SenseHat()

def _round_to_half(value):
    return round(value * 2.0) / 2.0


def get_temperature():
    return _round_to_half(sense.get_temperature())


def get_pressure():
    return round(sense.get_pressure())


def get_humidity():
    return round(sense.get_humidity())


def values_to_db():
    time = Time.objects.create(value=timezone.now())
    Temperature.objects.create(value=get_temperature(), time=time)
    Humidity.objects.create(value=get_humidity(), time=time)
    Pressure.objects.create(value=get_pressure(), time=time)
