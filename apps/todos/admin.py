from django.contrib import admin
from apps.todos.models import Todo


# admin.site.register(Todo)
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
