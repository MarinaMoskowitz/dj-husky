from rest_framework import serializers
from djhuskyapp.models import Party, Song


# noinspection PyAbstractClass
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_id', 'party', 'track_id', 'upvotes', 'downvotes', 'played')


# noinspection PyAbstractClass
class PartySerializer(serializers.ModelSerializer):
    # songs = serializers.StringRelatedField(many=True)
    songs = SongSerializer(many=True)

    class Meta:
        model = Party
        fields = ('party_id', 'name', 'songs')
