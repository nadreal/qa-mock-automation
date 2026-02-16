import pytest
from tests.schemas.user_schema import UserCreatePayload, UserResponse

@pytest.mark.api
def test_create_user(user_client, unique_user_id):    
    payload = UserCreatePayload(id=unique_user_id, name="Stevan", role="user")    
    
    response = user_client.create_user(payload.model_dump())
     
    assert response.model_dump() == payload.model_dump()
   
@pytest.mark.api
def test_list_users(user_client, unique_user_id):    
    users_payload = [
        {"id": unique_user_id, "name": "Stevan", "role": "user"},
        {"id": unique_user_id + 1, "name": "Jovanka", "role": "user"}
    ]
    for u in users_payload:
        user_client.create_user(u)

    users = user_client.get_users()
    
    returned_ids = {u.id for u in users}
    expected_ids = {u["id"] for u in users_payload}
    assert expected_ids.issubset(returned_ids), "Not all created users are returned"

    user_dicts = [u.model_dump() for u in users]
    for u in users_payload:
        assert u in user_dicts, f"User {u['id']} data mismatch"

@pytest.mark.api
def test_delete_user(user_client, unique_user_id):
    payload = UserCreatePayload(id=unique_user_id, name="Laki", role="user")    
    user_client.create_user(payload.model_dump())
    
    delete_response = user_client.delete_user(unique_user_id, raw_response=True)    
    assert delete_response.status_code == 204
    
    get_response = user_client.get_user(unique_user_id, raw_response=True)
    assert get_response.status_code == 404

@pytest.mark.api
def test_get_user(user_client, unique_user_id):    
    payload = UserCreatePayload (id=unique_user_id, name="Jovanka",role="user")
    user_client.create_user(payload.model_dump()) 
    
    user = user_client.get_user(unique_user_id)
    assert user.model_dump() == payload.model_dump()
   
@pytest.mark.api_negative
def test_get_missing_user(user_client):
    response = user_client.get_user(999, raw_response=True)
    assert response.status_code == 404

@pytest.mark.api_negative
def test_delete_missing_user(user_client):
    response = user_client.delete_user(999, raw_response=True)
    assert response.status_code == 404

@pytest.mark.api_negative
def test_duplicate_user(user_client, unique_user_id):
    payload = UserCreatePayload(id=unique_user_id, name="Dup", role="user")
    user_client.create_user(payload.model_dump())
    response = user_client.create_user(payload.model_dump(), raw_response=True)
    assert response.status_code == 400
    assert "already exists" in response.text.lower()
    
@pytest.mark.api_negative
def test_create_user_missing_required_fields(user_client):   
    invalid_payload = {} 
    
    response = user_client.create_user(invalid_payload, raw_response=True)
    assert response.status_code == 422
    
    body = response.json()
    assert "detail" in body
    
    detail = body["detail"]    
    missing_fields = {item["loc"][-1] for item in detail}    
    
    required_fields = set(UserCreatePayload.model_fields.keys())
    assert required_fields <= missing_fields   
    
    
@pytest.mark.api_negative
def test_create_user_with_wrong_id_type(user_client):    
    payload = {"id": "pera", "name": "Pera", "role":"user"}
    response = user_client.create_user(payload=payload, raw_response=True)
    assert response.status_code == 422
    assert "detail" in response.json()
    detail = response.json()["detail"]
    fields = [item["loc"][-1] for item in detail]
    
    id_errors = [item for item in detail if item["loc"][-1] == "id"]    
    assert id_errors
    assert id_errors[0]["type"] in {"int_parsing", "type_error.integer"}

@pytest.mark.parametrize("payload", [
    {"id": None, "name": "Test", "role": "user"},
    {"id": "abc", "name": "Test", "role": "user"},
    {"name": "Test"},
])
@pytest.mark.api_negative
def test_invalid_user_payloads(user_client, payload):
    response = user_client.create_user(payload, raw_response=True)
    assert response.status_code == 422
            
    