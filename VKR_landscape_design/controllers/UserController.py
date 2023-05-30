from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response, HTTPException
import json
from base_models import User
from models.users_model import *
from utils import get_db_connection
router = APIRouter()


@router.get("/users/one")
async def users_get_one_user(user_id: int):
    conn = get_db_connection()
    x = get_one_user(conn, user_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: пользователь с данным ID не найден.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/users/onewithoutpassword")
async def users_get_one_user_without_password(user_id: int):
    conn = get_db_connection()
    x = get_one_user_without_password(conn, user_id)
    if len(x) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: пользователь с данным ID не найден.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)


@router.post("/users/authorisation/")
async def users_post_authorisation(user: User.UserAuthorization):
    conn = get_db_connection()
    x = authorisation(conn, user.user_login, user.user_password)
    if len(x) == 0:
        raise HTTPException(status_code=401, detail="Ошибка: неправильный логин или пароль.")
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/users/all")
async def users_get_select_all():
    conn = get_db_connection()
    x = get_users(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/users/allwithoutpassword")
async def users_get_select_all_without_password():
    conn = get_db_connection()
    x = get_users_without_password(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/users/allwithoutpasswordadmins")
async def users_get_select_all_without_password():
    conn = get_db_connection()
    x = get_users_without_password_admins(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/users/allwithoutpasswordnoadmins")
async def users_get_select_all_without_password():
    conn = get_db_connection()
    x = get_users_without_password_noadmins(conn)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.post("/users/delete")
async def users_post_delete(user_id: int):
    conn = get_db_connection()
    y = get_one_user(conn, user_id)
    if len(y) == 0:
        raise HTTPException(status_code=404, detail="Ошибка: пользователь с данным ID не найден, потому удалить его невозможно.")
    x = delete_user(conn, user_id)
    return Response("{'messdelete':'Пользователь удалён.'}", status_code=200)

@router.post("/users/insert")
async def users_post_insert(user: User.UserRegister):
    conn = get_db_connection()
    if ((len(user.user_login) < 2) or (len(user.user_login) > 20)):
        raise HTTPException(status_code=400, detail="Ошибка: логин пользователя должен иметь длину от 2 до 20 символов (включительно).")
    if ((len(user.user_password) < 4) or (len(user.user_password) > 20)):
        raise HTTPException(status_code=400, detail="Ошибка: пароль пользователя должен иметь длину от 4 до 20 символов (включительно).")
    if ((len(user.user_email) < 6) or (len(user.user_email) > 30) or (not('@' in user.user_email))):
        raise HTTPException(status_code=400, detail="Ошибка: электронная почта пользователя должна иметь длину от 6 до 30 символов (включительно) и содержать символ @.")
    y = find_user_login(conn, user.user_login)
    if len(y) != 0:
        raise HTTPException(status_code=400, detail="Ошибка: пользователь с таким логином уже есть в системе. Введите другой логин.")
    z = find_user_email(conn, user.user_email)
    if len(z) != 0:
        raise HTTPException(status_code=400, detail="Ошибка: на эту электронную почту уже был зарегистрирован аккаунт пользователя. Введите другую электронную почту.")
    x = insert_user(conn, user.user_login, user.user_password, user.user_email)
    return Response("{'messinsert':'Пользователь создан.'}", status_code=200)

@router.post("/users/update/login")
async def users_post_update_login(user_id: int, user_login: str):
    conn = get_db_connection()
    if ((len(user_login) < 2) or (len(user_login) > 20)):
        raise HTTPException(status_code=400, detail="Ошибка: логин пользователя должен иметь длину от 2 до 20 символов (включительно).")
    y = find_user_login(conn, user_login)
    if len(y) != 0:
        raise HTTPException(status_code=400, detail="Ошибка: пользователь с таким логином уже есть в системе. Введите другой логин.")
    x = update_user_login(conn, user_id, user_login)
    return Response("{'messlogin':'Логин пользователя обновлён.'}", status_code=200)

@router.post("/users/update/password")
async def users_post_update_password(user_id: int, user_password: str):
    conn = get_db_connection()
    if ((len(user_password) < 4) or (len(user_password) > 20)):
        raise HTTPException(status_code=400, detail="Ошибка: пароль пользователя должен иметь длину от 4 до 20 символов (включительно).")
    x = update_user_password(conn, user_id, user_password)
    return Response("{'messpassword':'Пароль пользователя обновлён.'}", status_code=200)

@router.post("/users/update/email")
async def users_post_update_email(user_id: int, user_email: str):
    conn = get_db_connection()
    if ((len(user_email) < 6) or (len(user_email) > 30) or (not('@' in user_email))):
        raise HTTPException(status_code=400, detail="Ошибка: электронная почта пользователя должна иметь длину от 6 до 30 символов (включительно) и содержать символ @.")
    z = find_user_email(conn, user_email)
    if len(z) != 0:
        raise HTTPException(status_code=400, detail="Ошибка: на эту электронную почту уже был зарегистрирован аккаунт пользователя. Введите другую электронную почту.")
    x = update_user_email(conn, user_id, user_email)
    return Response("{'messemail':'Электронная почта пользователя обновлена.'}", status_code=200)

@router.post("/users/update/surname")
async def users_post_update_surname(user_id: int, user_surname: str):
    conn = get_db_connection()
    if ((len(user_surname) < 2) or (len(user_surname) > 20) or (not(user_surname[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: фамилия пользователя должна иметь длину от 2 до 20 символов (включительно), а её первая буква должна быть заглавной.")
    x = update_user_surname(conn, user_id, user_surname)
    return Response("{'messsurname':'Фамилия пользователя обновлена.'}", status_code=200)

@router.post("/users/update/name")
async def users_post_update_name(user_id: int, user_name: str):
    conn = get_db_connection()
    if ((len(user_name) < 2) or (len(user_name) > 20) or (not(user_name[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: имя пользователя должно иметь длину от 2 до 20 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_user_name(conn, user_id, user_name)
    return Response("{'messname':'Имя пользователя обновлено.'}", status_code=200)

@router.post("/users/update/fathername")
async def users_post_update_fathername(user_id: int, user_fathername: str):
    conn = get_db_connection()
    if ((len(user_fathername) < 2) or (len(user_fathername) > 20) or (not(user_fathername[0].isupper()))):
        raise HTTPException(status_code=400, detail="Ошибка: отчество пользователя должно иметь длину от 2 до 20 символов (включительно), а его первая буква должна быть заглавной.")
    x = update_user_fathername(conn, user_id, user_fathername)
    return Response("{'messfathername':'Отчество пользователя обновлено.'}", status_code=200)

@router.post("/users/update/age")
async def users_post_update_age(user_id: int, user_age: int):
    conn = get_db_connection()
    if ((user_age < 3) or (user_age > 120)):
        raise HTTPException(status_code=400, detail="Ошибка: возраст пользователя должен быть от 3 до 120 лет (включительно).")
    x = update_user_age(conn, user_id, user_age)
    return Response("{'message':'Возраст пользователя обновлён.'}", status_code=200)

@router.post("/users/update/isFemale")
async def users_post_update_isFemale(user_id: int, user_isFemale: int):
    conn = get_db_connection()
    if ((user_isFemale < 0) or (user_isFemale > 1)):
        raise HTTPException(status_code=400, detail="Ошибка: пол пользователя может быть только 0 (мужчина) или 1 (женщина).")
    x = update_user_isFemale(conn, user_id, user_isFemale)
    return Response("{'messisFemale':'Обновлено, является ли пользователь женщиной.'}", status_code=200)

@router.post("/users/update/picture")
async def users_post_update_picture(user: User.UserPicture):
    """
      Описание: изменение картинки (аватарки) пользователя.
      Ограничение на вход: файл с картинкой (аватаркой) пользователя не должен содержать более 100000 символов.
    """
    conn = get_db_connection()
    if (len(user.user_picture) > 100000):
        raise HTTPException(status_code=400, detail="Ошибка: файл с картинкой (аватаркой) пользователя не должен содержать более 100000 символов.")
    x = update_user_picture(conn, user.user_id, user.user_picture)
    return Response("{'messpicture':'Картинка пользователя обновлена.'}", status_code=200)

@router.post("/users/update/isAdmin")
async def users_post_update_isAdmin(user_id: int, user_isAdmin: int):
    conn = get_db_connection()
    if ((user_isAdmin < 0) or (user_isAdmin > 1)):
        raise HTTPException(status_code=400, detail="Ошибка: пользователь может быть только или обычным (0), или администратором (1).")
    x = update_user_isAdmin(conn, user_id, user_isAdmin)
    return Response("{'messisAdmin':'Обновлено, является ли пользователь администратором.'}", status_code=200)