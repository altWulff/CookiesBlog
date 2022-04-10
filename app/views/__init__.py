from fastapi import APIRouter


from . import index, user, post


views = APIRouter()
views.include_router(index.router, tags=['index'])
views.include_router(user.router, tags=['user'])
views.include_router(post.router, tags=['post'])
