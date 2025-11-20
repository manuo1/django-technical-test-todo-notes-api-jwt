from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Auth (JWT)
    path("api/auth/", include("config.auth_urls")),
    # Notes
    path("api/notes/", include("notes.api.urls")),
    # Todos
    path("api/todos/", include("todos.api.urls")),
]
