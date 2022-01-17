from tradebook.models import Note
from django.shortcuts import render
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def note_list(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view()
def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)
