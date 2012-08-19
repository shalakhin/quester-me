from django.contrib.gis.db import models
from django.contrib.auth.models import User
from quest.models import Address


# Create your models here.

USER_POSITION_TYPE = (
    ('IP', 'By ip address'),
    ('BR', 'By browser'),
)


class UserPosition(models.Model):
    user = models.OneToOneField(User)
    address = models.ForeignKey(Address, blank=True, null=True)
    point = models.PointField()
    type = models.CharField(choices=USER_POSITION_TYPE, max_length=2)
    updated = models.DateTimeField(auto_now=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return "Position for user %d" % self.user_id
