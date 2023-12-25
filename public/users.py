from fastapi import APIRouter, Body
from models.models import MainUser, MainUserDB, NewResponse
from typing import Union, Annotated

users_router = APIRouter()


# Функция для работы с паролями
def code_password(code: str):
    result = code * 2


# База данных для практики
users_list = [MainUserDB(name='Ivanov', id=108, password='ivan12341234'),
              MainUserDB(name="Petrov", id=134, password="petr12341234")]


# Поиск пользователя в списке
def find_user(id: int) -> Union[MainUserDB, MainUserDB, None]:
    """Поиск пользователя в списке"""
    for user in users_list:
        if user.id == id:
            return user
    return None


# Вывод списка пользователей

@users_router.get("/api/users", response_model=Union[list[MainUser], list[MainUserDB], None])
def get_users():
    """Вывод списка пользователей"""
    return users_list


# Получение отдельного пользователя

@users_router.get("/api/users/{id}", response_model=Union[MainUser, MainUserDB, NewResponse])
def get_user(id: int):
    """Получение отдельного пользователя"""
    user = find_user(id)
    print(user)
    if user is None:
        return NewResponse(message="Пользователь не найден")
    return user


# Создание нового пользователя с соответствующими параметрами

@users_router.post("/api/users", response_model=Union[MainUser, MainUserDB, NewResponse])
def create_user(item: Annotated[MainUser, MainUserDB, Body(embed=True, description="Новый пользователь")]):
    """Создание нового пользователя с соответствующими параметрами"""
    user = MainUserDB(name=item.name, id=item.id, password=item.password)
    users_list.append(user)
    return user


# Обновление информации о пользователе

@users_router.put("/api/users", response_model=Union[MainUser, MainUserDB, NewResponse])
def edit_person(
        item: Annotated[MainUser, MainUserDB, Body(embed=True, description="Изменяем данные для пользователя по id")]):
    """Обновление информации о пользователе"""
    user = find_user(item.id)
    if user is None:
        return NewResponse(message="Пользователь не найден")
    user.id = item.id
    user.name = item.name
    user.password = item.password
    return user


# Удаление пользователя из базы

@users_router.delete("/api/users/{id}", response_model=Union[list[MainUser], list[MainUserDB], None])
def delete_person(id: int):
    """ Удаление пользователя из базы"""
    user = find_user(id)
    if user is None:
        return NewResponse(message="Пользователь не найден")

    users_list.remove(user)
    return users_list
