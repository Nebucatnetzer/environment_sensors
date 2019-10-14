from django.db import models


class Time(models.Model):
    value = models.DateTimeField()


class Temperature(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    value = models.FloatField()


class Humidity(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    value = models.FloatField()


class Pressure(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    value = models.FloatField()

