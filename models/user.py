from pydantic import BaseModel, PositiveInt
class User(BaseModel):
  fullname : str
  websiteurl: str
  phonenumber: int
  email: str
  
