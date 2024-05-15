from pydantic import BaseModel


class User(BaseModel):
    id: int | None = None
    firstname: str
    lastname: str
    email: str
    phone: int
    password: str

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "firstname": "Carl",
                "lastname": "Johnson",
                "email": "carljohnson@gmail.com",
                "phone": "6143520331",
                "password": "Mypassword123"
            }
        }


class LoginModel(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True,
        json_schema_extra = {
            "example": {
                "email": "example@gmail.com",
                "password": "Examplepassword123"
            }
        }


class RegisterModel(User):
    pass
