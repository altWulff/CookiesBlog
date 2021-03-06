from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse
from starlette_wtf import csrf_protect
from app.schemas import UserCreate
from app.forms import RegisterUserForm, LoginUserForm
from app.db import SessionLocal
from app.config.jinja_env import templates, flash
from app.api.login import login_access_token
import app.crud as crud


router = APIRouter()


@router.route('/register', methods=['GET', 'POST'])
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
        crud.user.create(db, user)
        flash(request, message='New user register', category='info')
        return RedirectResponse(url='/', status_code=303)

    return_status_code = 422 if form.errors else 200
    return templates.TemplateResponse(
        "user/register.html",
        {"request": request, 'form': form},
        status_code=return_status_code
    )


@router.route('/login', methods=['GET', 'POST'])
@csrf_protect
async def login_account(request: Request):
    form = await LoginUserForm.from_formdata(request)
    if await form.validate_on_submit():
        db = SessionLocal()
        login_access_token(db, form)
        flash(
            request,
            message=f'User Login: {form.username.data}',
            category='info'
        )
        return RedirectResponse(url='/', status_code=303)

    return_status_code = 422 if form.errors else 200
    return templates.TemplateResponse(
            "user/login.html",
            {"request": request, 'form': form},
            status_code=return_status_code
        )
