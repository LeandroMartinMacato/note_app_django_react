from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

#RESTFUL VERSION OF ROUTES
# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE


@api_view(['GET'])
def getRoutes(requests):
    ''' Return possibles API routes '''
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {
                'body': ""
            },
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint':
            '/notes/id/update/',
            'method':
            'PUT',
            'body': {
                'body': ""
            },
            'description':
            'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(requests):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')


@api_view(['POST'])
def createNote(request):
    ''' .... '''
    new_note = "I AM A NEW NOTE"
    return new_note
