from django.shortcuts import render


from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from djhuskyapp.models import Party, Song
from djhuskyapp.serializers import PartySerializer, SongSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class PartyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class SongViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
