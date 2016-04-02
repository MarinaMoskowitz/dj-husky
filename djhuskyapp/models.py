from __future__ import unicode_literals

from django.db import models


# Keeps track of the unique parties
class Party(models.Model):
    party_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return '{0}, {1}'.format(self.party_id, self.name)


# The individual songs, each associated with a unique party
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    party = models.ForeignKey(Party, related_name='songs', on_delete=models.CASCADE)
    track_id = models.CharField(max_length=100)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    class Meta:
        unique_together = ('party', 'track_id')

    def __unicode__(self):
        return '{0}, {1}, {2}, {3}'.format(self.song_id, self.upvotes, self.downvotes, self.track_id)
