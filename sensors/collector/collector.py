import os
import datetime

if os.uname()[4].startswith("arm"):
    from sense_hat import SenseHat
else:
    from sense_emu import SenseHat

from .models import Time, Temperature, Humidity, Pressure

sense = SenseHat()


def get_temperature():
    raw_temp = sense.get_temperature()
    return round(raw_temp, 1)


def get_pressure():
    raw_pressure = sense.get_pressure()
    return round(raw_pressure, 1)


def get_humidity():
    raw_humidity = sense.get_humidity()
    return round(raw_humidity, 1)


def values_to_db():
    time = Time.objects.create(value=datetime.datetime.now())
    Temperature.objects.create(value=get_temperature(), time=time)
    Humidity.objects.create(value=get_humidity(), time=time)
    Pressure.objects.create(value=get_pressure(), time=time)
