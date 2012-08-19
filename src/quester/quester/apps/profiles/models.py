from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from quest.models import Quest


class Profile(models.Model):
    """
        Custom user profile for additional info
    """

    user = models.OneToOneField(User)

    experience = models.PositiveIntegerField(verbose_name='experience',
        default=0)
    quests = models.ManyToManyField(Quest, verbose_name='quests',
        related_name='quests', null=True)

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
