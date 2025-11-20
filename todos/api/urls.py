from rest_framework.routers import DefaultRouter

from todos.api.views import TodoViewSet

router = DefaultRouter()
router.register(r"", TodoViewSet, basename="todo")
urlpatterns = router.urls
