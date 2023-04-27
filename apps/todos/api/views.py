from rest_framework.viewsets import ModelViewSet
from apps.todos.models import Todo
from apps.todos.api.serializers import TodoSerializer


class TodoApiViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
