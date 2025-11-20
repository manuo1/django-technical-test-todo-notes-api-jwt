from rest_framework.routers import DefaultRouter

from notes.api.views import NoteViewSet

router = DefaultRouter()
router.register(r"", NoteViewSet, basename="note")

urlpatterns = router.urls
