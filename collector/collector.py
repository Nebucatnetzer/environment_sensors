import os
from datetime import datetime, timedelta

if os.uname()[4].startswith("arm"):
    from sense_hat import SenseHat
else:
    from sense_emu import SenseHat

from .models import Temperature, Humidity, Pressure

sense = SenseHat()

def _round_to_half(value):
    return round(value * 2.0) / 2.0


def get_temperature():
    return round(0.899338368784139 * sense.get_temperature(), 1)


def get_pressure():
    return round(sense.get_pressure())


def get_humidity():
    return round(sense.get_humidity())


def values_to_db():
    time = datetime.now()
    Temperature.objects.create(value=get_temperature(), time=time)
    Humidity.objects.create(value=get_humidity(), time=time)
    Pressure.objects.create(value=get_pressure(), time=time)


def clean_db():
    time = datetime.now() - timedelta(days=30)
    Temperature.objects.filter(time__lt=time).delete()
    Humidity.objects.filter(time__lt=time).delete()
    Pressure.objects.filter(time__lt=time).delete()
