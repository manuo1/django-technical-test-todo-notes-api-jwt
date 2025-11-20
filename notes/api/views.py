from rest_framework import viewsets

from notes.api.serializers import NoteSerializer
from notes.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    """
    REST ViewSet.

    Endpoints:
    - GET    /api/notes/          -> list
    - POST   /api/notes/          -> create
    - GET    /api/notes/{id}/     -> retrieve
    - PUT    /api/notes/{id}/     -> update
    - PATCH  /api/notes/{id}/     -> partial_update
    - DELETE /api/notes/{id}/     -> destroy
    """

    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer
