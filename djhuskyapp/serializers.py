from rest_framework import serializers
from djhuskyapp.models import Party, Song


# noinspection PyAbstractClass
class PartySerializer(serializers.ModelSerializer):
    songs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Party
        fields = ('party_id', 'name', 'songs')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Party` instance, given the validated data.
    #     :param validated_data: the data that has been validated
    #     """
    #     return Party.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Party` instance, given the validated data.
    #     :param instance: the 'Party' instance
    #     :param validated_data: the data that has been validated
    #     """
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance
    #
    # def to_representation(self, value):
    #     return super(PartySerializer, self).to_representation(value)
    #
    # def to_internal_value(self, data):
    #     pass


# noinspection PyAbstractClass
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_id', 'party', 'track_id', 'upvotes', 'downvotes')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Song` instance, given the validated data.
    #     :param validated_data: the data that has been validated
    #     """
    #     return Song.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Song` instance, given the validated data.
    #     :param instance: the 'Song' instance
    #     :param validated_data: the data that has been validated
    #     """
    #     instance.upvotes = validated_data.get('upvotes', instance.upvotes)
    #     instance.downvotes = validated_data.get('downvotes', instance.downvotes)
    #     instance.save()
    #     return instance
    #
    # def to_representation(self, value):
    #     return super(SongSerializer, self).to_representation(value)
    #
    # def to_internal_value(self, data):
    #     pass
