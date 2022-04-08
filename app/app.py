from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_wtf import CSRFProtectMiddleware, csrf_protect
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from config import settings
from fastapi.staticfiles import StaticFiles

import crud
from database import engine, get_db, SessionLocal
from schemas import User, UserCreate, PostCreate
from models import Base
from forms import RegisterUserForm, LoginUserForm, NewPostForm


def flash(request: Request, message: ..., category: str = "") -> None:
    if "_messages" not in request.session:
        request.session["_messages"] = []
    request.session["_messages"].append({"message": message, "category": category})


def get_flashed_messages(request: Request):
    print(request.session)
    return request.session.pop("_messages") if "_messages" in request.session else []


Base.metadata.create_all(bind=engine)
middleware = [
    Middleware(SessionMiddleware, secret_key=settings.SECRET_KEY),
    Middleware(CSRFProtectMiddleware, csrf_secret=settings.CSRF_KEY)
]
app = FastAPI(title='Cookies Blog', middleware=middleware)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
templates.env.globals['get_flashed_messages'] = get_flashed_messages


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.route('/register', methods=['GET', 'POST'])
@csrf_protect
async def create_account(request: Request):
    form = await RegisterUserForm.from_formdata(request)
    if await form.validate_on_submit():
        user = UserCreate(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db = SessionLocal()
        crud.create_user(db, user)
        flash(request, message='New user register', category='info')
        return RedirectResponse(url='/', status_code=303)

    return_status_code = 422 if form.errors else 200
    return templates.TemplateResponse(
        "user/register.html",
        {"request": request, 'form': form},
        status_code=return_status_code
    )


@app.route('/login', methods=['GET', 'POST'])
@csrf_protect
async def login_account(request: Request):
    form = await LoginUserForm.from_formdata(request)
    if await form.validate_on_submit():
        db = SessionLocal()
        # TODO login function
        flash(request, message=f'User Login: {form.username.data}', category='info')
        return RedirectResponse(url='/', status_code=303)

    return_status_code = 422 if form.errors else 200
    return templates.TemplateResponse(
            "user/login.html",
            {"request": request, 'form': form},
            status_code=return_status_code
        )


@app.route('/post/new', methods=['GET', 'POST'])
@csrf_protect
async def create_new_post(request: Request):
    form = await NewPostForm.from_formdata(request)
    if await form.validate_on_submit():
        user = PostCreate(
            title=form.title.data,
            body=form.body.data,
        )
        flash(request, message='New post create', category='info')
        return RedirectResponse(url='/', status_code=303)

    return_status_code = 422 if form.errors else 200
    return templates.TemplateResponse(
        "post/new.html",
        {"request": request, 'form': form},
        status_code=return_status_code
    )
