from rest_framework.routers import DefaultRouter
from apps.todos.api.views import TodoApiViewSet

router_todos = DefaultRouter()
router_todos.register(prefix="todos", basename="todos", viewset=TodoApiViewSet)
