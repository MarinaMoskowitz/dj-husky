from rest_framework import serializers
from djhuskyapp.models import Party, Song


# noinspection PyAbstractClass
class PartySerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Party
        fields = ('party_id', 'name', 'songs')


# noinspection PyAbstractClass
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_id', 'party', 'track_id', 'upvotes', 'downvotes')
