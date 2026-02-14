from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """Модель данных пользователя."""

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """Запрос на создание пользователя."""

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """Ответ с данными созданного пользователя."""

    user: UserSchema
