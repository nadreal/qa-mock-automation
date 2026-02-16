import pytest

@pytest.mark.api
def test_health(admin_client):
    response = admin_client.get_admin_stats(raw_response=True)    
    assert response.status_code == 200    
    
    data = response.json()
    assert data == {"status": "ok"}, "Response body mismatch"