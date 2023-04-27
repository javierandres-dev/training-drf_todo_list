from rest_framework.serializers import ModelSerializer
from apps.todos.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed"]
