from django.shortcuts import render


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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


@csrf_exempt
def party_list(request):
    """
    List all parties, or create a new party.
    :param request: the request
    """
    if request.method == 'GET':
        party = Party.objects.all()
        serializer = PartySerializer(party, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PartySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def song_list(request):
    """
    List all songs, or create a new song.
    :param request: the request
    """
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def party_detail(request, pk):
    """
    Retrieve, update or delete a party.
    :param request: the request
    :param pk: the party primary key
    """
    try:
        party = Party.objects.get(pk=pk)
    except Party.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PartySerializer(party)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PartySerializer(party, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        party.delete()
        return HttpResponse(status=204)


@csrf_exempt
def song_detail(request, pk):
    """
    Retrieve, update or delete a song.
    :param request: the request
    :param pk: the song primary key
    """
    try:
        song = Song.objects.get(pk=pk)
    except Song.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SongSerializer(song, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        song.delete()
        return HttpResponse(status=204)
