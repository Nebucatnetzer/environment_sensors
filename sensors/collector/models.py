from django.db import models

# Create your models here.
class Time(models.Model):
    value = DateTimeField()


class Temperatur(models.Model):
    time = ForeignKeyField(Time, backref='temperatures')
    value = FloatField()


class Humidity(models.Model):
    time = ForeignKeyField(Time, backref='humidities')
    value = FloatField()


class Pressure(models.Model):
    time = ForeignKeyField(Time, backref='pressures')
    value = FloatField()

