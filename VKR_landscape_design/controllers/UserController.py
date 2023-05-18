from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, Response
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
        return Response("{'message':'Пользователь с данным ID не найден.'}", status_code=401)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)

@router.get("/users/onewithoutpassword")
async def users_get_one_user_without_password(user_id: int):
    conn = get_db_connection()
    x = get_one_user_without_password(conn, user_id)
    if len(x) == 0:
        return Response("{'message':'Пользователь с данным ID не найден.'}", status_code=401)
    return Response(json.dumps(x.to_dict(orient="records")), status_code=200)


@router.post("/users/authorisation/")
async def users_post_authorisation(user: User.UserAuthorization):
    conn = get_db_connection()
    x = authorisation(conn, user.user_login, user.user_password)
    if len(x) == 0:
        return Response("{'message':'Неправильный логин или пароль.'}", status_code=401)
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
    x = delete_user(conn, user_id)
    return Response("{'messdelete':'Пользователь удалён.'}", status_code=200)

@router.post("/users/insert")
async def users_post_insert(user: User.UserRegister):
    conn = get_db_connection()
    x = insert_user(conn, user.user_login, user.user_password, user.user_email)
    return Response("{'messinsert':'Пользователь создан.'}", status_code=200)

@router.post("/users/update/login")
async def users_post_update_login(user_id: int, user_login: str):
    conn = get_db_connection()
    x = update_user_login(conn, user_id, user_login)
    return Response("{'messlogin':'Логин пользователя обновлён.'}", status_code=200)

@router.post("/users/update/password")
async def users_post_update_password(user_id: int, user_password: str):
    conn = get_db_connection()
    x = update_user_password(conn, user_id, user_password)
    return Response("{'messpassword':'Пароль пользователя обновлён.'}", status_code=200)

@router.post("/users/update/email")
async def users_post_update_email(user_id: int, user_email: str):
    conn = get_db_connection()
    x = update_user_email(conn, user_id, user_email)
    return Response("{'messemail':'Электронная почта пользователя обновлена.'}", status_code=200)

@router.post("/users/update/surname")
async def users_post_update_surname(user_id: int, user_surname: str):
    conn = get_db_connection()
    x = update_user_surname(conn, user_id, user_surname)
    return Response("{'messsurname':'Фамилия пользователя обновлена.'}", status_code=200)

@router.post("/users/update/name")
async def users_post_update_name(user_id: int, user_name: str):
    conn = get_db_connection()
    x = update_user_name(conn, user_id, user_name)
    return Response("{'messname':'Имя пользователя обновлено.'}", status_code=200)

@router.post("/users/update/fathername")
async def users_post_update_fathername(user_id: int, user_fathername: str):
    conn = get_db_connection()
    x = update_user_fathername(conn, user_id, user_fathername)
    return Response("{'messfathername':'Отчество пользователя обновлено.'}", status_code=200)

@router.post("/users/update/age")
async def users_post_update_age(user_id: int, user_age: int):
    conn = get_db_connection()
    x = update_user_age(conn, user_id, user_age)
    return Response("{'message':'Возраст пользователя обновлён.'}", status_code=200)

@router.post("/users/update/isFemale")
async def users_post_update_isFemale(user_id: int, user_isFemale: int):
    conn = get_db_connection()
    x = update_user_isFemale(conn, user_id, user_isFemale)
    return Response("{'messisFemale':'Обновлено, является ли пользователь женщиной.'}", status_code=200)

@router.post("/users/update/picture")
async def users_post_update_picture(user_id: int, user_picture: str):
    conn = get_db_connection()
    x = update_user_picture(conn, user_id, user_picture)
    return Response("{'messpicture':'Картинка пользователя обновлена.'}", status_code=200)

@router.post("/users/update/isAdmin")
async def users_post_update_isAdmin(user_id: int, user_isAdmin: int):
    conn = get_db_connection()
    x = update_user_isAdmin(conn, user_id, user_isAdmin)
    return Response("{'messisAdmin':'Обновлено, является ли пользователь администратором.'}", status_code=200)