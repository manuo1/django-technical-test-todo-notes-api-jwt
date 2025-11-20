from rest_framework import viewsets

from todos.api.serializers import TodoSerializer
from todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    """
    REST ViewSet for Todos.
    Endpoints:
    - GET    /api/todos/          -> list
    - POST   /api/todos/          -> create
    - GET    /api/todos/{id}/     -> retrieve
    - PUT    /api/todos/{id}/     -> update
    - PATCH  /api/todos/{id}/     -> partial_update
    - DELETE /api/todos/{id}/     -> destroy
    """

    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
