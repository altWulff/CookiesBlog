from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_wtf import CSRFProtectMiddleware, csrf_protect
from config import settings
from fastapi.staticfiles import StaticFiles
from db import engine
from db import Base


Base.metadata.create_all(bind=engine)
middleware = [
    Middleware(SessionMiddleware, secret_key=settings.SECRET_KEY),
    Middleware(CSRFProtectMiddleware, csrf_secret=settings.CSRF_KEY)
]
app = FastAPI(title='Cookies Blog', middleware=middleware)
app.mount("/static", StaticFiles(directory="static"), name="static")


from views import views
app.include_router(views)
