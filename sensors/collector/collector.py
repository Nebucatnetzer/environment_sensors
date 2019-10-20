import os

if os.uname()[4].startswith("arm"):
    from sense_hat import SenseHat
else:
    from sense_emu import SenseHat

sense = SenseHat()


def get_temperature():
    raw_temp = sense.get_temperature()
    return round(raw_temp, 1)


def get_pressure():
    return sense.get_pressure()


def get_humidity():
    return sense.get_humidity()
