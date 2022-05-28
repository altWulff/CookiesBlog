from fastapi import APIRouter, Request, status
from starlette.responses import RedirectResponse
from starlette_wtf import csrf_protect

import app.crud as crud
from app.config.jinja_env import flash, templates
from app.forms import NewPostForm
from app.schemas import Post

router = APIRouter()


@router.route("/post/new", methods=["GET", "POST"])
@csrf_protect
async def create_new_post(request: Request):
    form = await NewPostForm.from_formdata(request)
    if await form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
        )
        crud.post.create_with_user(0, post)
        flash(request, message="New post create", category="info")
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY if form.errors else 200
    return templates.TemplateResponse(
        "post/new.html",
        {"request": request, "form": form},
        status_code=status_code,
    )
