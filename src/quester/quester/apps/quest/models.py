from django.contrib.gis.db import models
from django_countries import CountryField

QUEST_CHOICES = (
    ('O', 'One point quest'),
    ('C', 'Chain quest'),
)

QUEST_DIFFICULTY_LEVEL = (
    ('0', 'Easy quest'),
    ('1', 'Medium quest'),
    ('2', 'Hard quest')
)


class Quest(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(choices=QUEST_CHOICES, max_length=1)
    difficulty_level = models.CharField(choices=QUEST_DIFFICULTY_LEVEL, max_length=2, blank=True, default='0')

    def __unicode__(self):
        return self.name


class Address(models.Model):
    num = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField()
    zipcode = models.CharField(max_length=10, blank=True, null=True)


    objects = models.GeoManager()

    def __unicode__(self):
        return "Address obj at %s" % self.country

class Marker(models.Model):
    quest = models.ForeignKey(Quest)
    address = models.ForeignKey(Address)

    point = models.PointField()

    objects = models.GeoManager()


