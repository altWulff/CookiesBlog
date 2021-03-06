from fastapi import APIRouter


from . import user, post, login


api = APIRouter()
api.include_router(user.router, prefix='/users', tags=['users'])
api.include_router(post.router, prefix='/posts', tags=['posts'])
api.include_router(login.router, prefix='/login', tags=['login'])
