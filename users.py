from fastapi import APIRouter, Body ,Response, Cookie
from typing import Optional
from bson import ObjectId
from funcDB import MongoDB
from Object_Str import Foo

# อยู่ใน floder router

router = APIRouter()
db = MongoDB(database_name='edu', uri='mongodb://127.0.0.1:27017/')


@router.get('/')
async def index_users():
    users = db.find(collection='testone', query={})
    users = list(users)

    for obj in users:
        del obj['_id']
    # print(users)
    return {'users':users}

# เพิ่ม
@router.post('/add/')
async def add_user(payload: dict = Body(...)):
    Id = Foo(_id=ObjectId())
    # print(Id)
    Id = Id.dict()['id']
    payload['id']= Id
    db.insert_one(collection='testone', data=payload)
    return {'testone':"sucess"}

# แก้ไข
@router.put('/update/{id}')
async def update_user(id: str, payload :dict = Body(...)):
    query = {'id': {"$eq": id}}
    value = {'$set': payload}
    db.update_one(collection='testone', query=query, values=value)
    return {'message': 'suceess'}

# ลบ
@router.delete('/delete/{id}')
async def delete_user(id:str):
    query = {'id': {"$eq": id}}
    db.delete_one(collection='testone', query=query) 
    return {'message': 'sucess'}


@router.post('/check/')
async def check(profile: list= None):
    group = {'data':profile}
    # Id = Foo(_id=ObjectId())
    print(group)
    # Id = Id.dict()['id']
    # profile['id']= Id
    db.insert_one(collection='check',data=group)
    return {'check':"sucess"}

# @router.post("/cookie-and-object/")
# def create_cookie(response: Response, profile: list= None):
#     response.set_cookie(key="fakesession", value=profile)
#     print(response)
#     db.insert_one(collection='check',data=response)
#     return {"message": "succees"}
