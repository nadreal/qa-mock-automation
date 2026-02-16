import pytest
from backend.app.models import User
from backend.app.services.user_service_memory import InMemoryUserService


def test_create_and_get_user():
    service = InMemoryUserService()
    user = User(id=1, name="Stevan", role="user")

    service.create_user(user)
    fetched = service.get_user(1)

    assert fetched == user


def test_duplicate_user():
    service = InMemoryUserService()
    user = User(id=1, name="Stevan", role="user")

    service.create_user(user)
    with pytest.raises(ValueError):
        service.create_user(user)
