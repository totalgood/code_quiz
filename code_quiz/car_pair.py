#!/usr//bin/env python

form django.db import models

class Car(models.Model):
    make = models.ForeignKey("Make")
    color = models.TextField()
    car_model = models.ForeignKey("CarModel")
    feature = ManyToManyField(through="CarFeature")

class CarFeature(models.Model):
    from_id = ForeignKey
    to_id = ForeignKey
    price = FloatField


class CarModel(models.Model):
    name = models.TextField()
    make = models.ForeignKey("Make")

class Make(models.Model):
    location = models.ForeignKey("Location")
    volume = models.FloatField(null=True)

class Feature(models.Model):

class Location(models.Model):
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)
    address_1 = models.TextField()
    address_2 = models.TextField()
    state = models.CharField(max_length=2)
    # zipcode =

class Purchase

car = Purchase.objects.filter(date__lte=datetime.now() - datetime.timedelta(365*2))


list of candidates
list of job openings




