from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Party(models.Model):
    party_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    track_id = models.CharField(max_length=100)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.track_id
