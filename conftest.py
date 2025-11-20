import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def user(db):
    User = get_user_model()
    return User.objects.create_user(username="testuser", password="testpass123")


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_client_authenticated(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client
