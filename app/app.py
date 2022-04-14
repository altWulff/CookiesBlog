from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_wtf import CSRFProtectMiddleware, csrf_protect
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.db import engine, Base


Base.metadata.create_all(bind=engine)
middleware = [
    Middleware(SessionMiddleware, secret_key=settings.SECRET_KEY),
    Middleware(CSRFProtectMiddleware, csrf_secret=settings.CSRF_KEY)
]
app = FastAPI(title='Cookies Blog', middleware=middleware)
app.mount("/static", StaticFiles(directory="./app/static"), name="static")


from app.views import views
from app.api import api

app.include_router(views)
app.include_router(api)

