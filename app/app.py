from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_wtf import CSRFProtectMiddleware, csrf_protect

from app.config import settings

middleware = [
    Middleware(SessionMiddleware, secret_key=settings.SECRET_KEY),
    Middleware(CSRFProtectMiddleware, csrf_secret=settings.CSRF_KEY),
]
app = FastAPI(title="Cookies Blog", middleware=middleware)
app.mount("/static", StaticFiles(directory="./app/static"), name="static")


from app.api import api
from app.views import views

app.include_router(views)
app.include_router(api, prefix="/api")
