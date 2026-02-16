import pytest, random
from backend.app.main import app
from fastapi.testclient import TestClient
from backend.app.dependencies import user_service
from tests.clients.users_client import UsersClient
from tests.clients.admin_client import AdminClient

@pytest.fixture(scope="session")
def test_client():    
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_users():    
    user_service._users.clear()

@pytest.fixture
def user_client(test_client):
    return UsersClient(test_client)

@pytest.fixture
def admin_client(test_client):
    return AdminClient(test_client)

@pytest.fixture
def unique_user_id():    
    return random.randint(1000, 9999)