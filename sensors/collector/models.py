from django.db import models


class Temperature(models.Model):
    time = models.DateTimeField()
    value = models.FloatField()


class Humidity(models.Model):
    time = models.DateTimeField()
    value = models.FloatField()


class Pressure(models.Model):
    time = models.DateTimeField()
    value = models.FloatField()

