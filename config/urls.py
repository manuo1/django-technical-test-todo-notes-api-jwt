from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Auth (JWT)
    path(
        "api/auth/",
        include(
            [
                path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
                path(
                    "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
                ),
            ]
        ),
    ),
    # Apps
    # path("api/todos/", include("todos.urls")),
    # path("api/notes/", include("notes.urls")),
]
