from tests.schemas.user_schema import UserResponse

class AdminClient:
    def __init__(self, client):
        self.client = client
        
    def get_admin_stats(self, raw_response=False):
        response = self.client.get("/health")
        if raw_response:
            return response
        response.raise_for_status()        
        return response.json()