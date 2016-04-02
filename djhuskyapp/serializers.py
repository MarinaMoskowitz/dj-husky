from rest_framework import serializers
from djhuskyapp.models import Party, Song


class PartySerializer(serializers.Serializer):
    songs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Party
        fields = ('name', 'songs')

    def create(self, validated_data):
        """
        Create and return a new `Party` instance, given the validated data.
        :param validated_data: the data that has been validated
        """
        return Party.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Party` instance, given the validated data.
        :param instance: the 'Party' instance
        :param validated_data: the data that has been validated
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def to_representation(self, value):
        return super(PartySerializer, self).to_representation(value)

    def to_internal_value(self, data):
        pass


class SongSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    track_id = serializers.CharField
    upvotes = serializers.IntegerField
    downvotes = serializers.IntegerField

    def create(self, validated_data):
        """
        Create and return a new `Song` instance, given the validated data.
        :param validated_data: the data that has been validated
        """
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Song` instance, given the validated data.
        :param instance: the 'Song' instance
        :param validated_data: the data that has been validated
        """
        instance.upvotes = validated_data.get('upvotes', instance.upvotes)
        instance.downvotes = validated_data.get('downvotes', instance.downvotes)
        instance.save()
        return instance
    
    def to_representation(self, value):
        return super(SongSerializer, self).to_representation(value)

    def to_internal_value(self, data):
        pass