from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.response import Response
import json

from djhuskyapp.models import Party, Song
from djhuskyapp.serializers import PartySerializer, SongSerializer


class PartyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer

    @detail_route()
    def highest_rated(self, request, pk):
        party = Party.objects.get(party_id=pk)
        raw_data = PartySerializer(party)
        actual_data = raw_data.data
        # songs = actual_data['songs']
        # sorted(songs, key=lambda song: -(song['upvotes'] - song['downvotes']))
        # actual_data['songs'] = songs
        return Response(actual_data)


class SongViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
