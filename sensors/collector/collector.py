import os

if os.uname()[4].startswith("arm"):
    from sense_hat import SenseHat
else:
    from sense_emu import SenseHat

sense = SenseHat()

def _get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return float(res.replace('temp=', '').replace("'C\n", ''))

def get_temperature():
    humidity_temp = self._sense_hat.get_temperature_from_humidity()
    pressure_temp = self._sense_hat.get_temperature_from_pressure()
    cpu_temp = _get_cpu_temperature()
    avg_temp = ((humidity_temp + pressure_temp)
                / 2 if pressure_temp else humidity_temp)
    adj_temp = avg_temp - (cpu_temp - avg_temp) / 0.69
    return adj_temp


def get_pressure():
    return sense.get_pressure()


def get_humidity():
    return sense.get_humidity()
