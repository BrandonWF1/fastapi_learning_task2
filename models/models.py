from typing import Union, Annotated
from pydantic import BaseModel, Field


class MainUser(BaseModel):  # Пользователь
    name: Union[str, None] = None  # Имя пользователя
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)] = None  # Id пользователя


class MainUserDB(MainUser):  # Отдельная модель для пароля
    password: Annotated[Union[str, None], Field(min_length=8, max_length=200)] = None


class NewResponse(BaseModel):  # Ответ
    message: str
