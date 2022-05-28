from fastapi import APIRouter, Request, status
from starlette.responses import RedirectResponse
from starlette_wtf import csrf_protect

import app.crud as crud
# from app.api.login import login_access_token
from app.config.jinja_env import flash, templates
from app.forms import LoginUserForm, RegisterUserForm
from app.schemas import User

router = APIRouter()


@router.route("/register", methods=["GET", "POST"])
@csrf_protect
async def create_account(request: Request):
    form = await RegisterUserForm.from_formdata(request)
    if await form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        crud.user.create(user)
        flash(request, message="New user register", category="info")
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY if form.errors else 200
    return templates.TemplateResponse(
        "user/register.html",
        {"request": request, "form": form},
        status_code=status_code,
    )


@router.route("/login", methods=["GET", "POST"])
@csrf_protect
async def login_account(request: Request):
    form = await LoginUserForm.from_formdata(request)
    if await form.validate_on_submit():
        # login_access_token(form)
        flash(request, message=f"User Login: {form.username.data}", category="info")
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY if form.errors else 200
    return templates.TemplateResponse(
        "user/login.html",
        {"request": request, "form": form},
        status_code=status_code,
    )
