from pydantic import BaseModel, StrictInt

class UserResponse(BaseModel):
    id: StrictInt
    name: str
    role: str
    
class UserCreatePayload(BaseModel):
    id: StrictInt
    name: str
    role: str
    