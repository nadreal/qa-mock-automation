from tests.schemas.user_schema import UserResponse

class UsersClient:
    def __init__(self, client):
        self.client = client
    
    def create_user(self, payload, raw_response=False):
        response = self.client.post("/users/", json = payload)
        if raw_response:
            return response
        response.raise_for_status() 
        return UserResponse(**response.json())
    
    def get_user(self, user_id, raw_response=False):
        response = self.client.get(f"/users/{user_id}/")
        if raw_response:
            return response
        response.raise_for_status() 
        return UserResponse(**response.json())
    
    def get_users(self, raw_response=False):
        response = self.client.get(f"/users/")
        if raw_response:
            return response
        response.raise_for_status() 
        return [UserResponse(**u) for u in response.json()]
    
    def delete_user(self, user_id, raw_response=False):
        response = self.client.delete(f"/users/{user_id}")
        if raw_response:
            return response
        response.raise_for_status() 
        return [UserResponse(**u) for u in response.json()]
    
