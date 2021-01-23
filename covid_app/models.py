from django.db import models


class Person(models.Model):
    rank = models.CharField(max_length=7)
    lname = models.CharField(max_length=27)
    fname = models.CharField(max_length=21)
    branch = models.CharField(max_length=10)
    category = models.CharField(max_length=30)
    edipi = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.rank} {self.lname}, {self.fname}'


class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location


class Event(models.Model):
    initiator = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    arrived = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Initiator: {self.initiator} - {self.arrived}'


class Scanner(models.Model):
    barcode = models.CharField(max_length=90)
