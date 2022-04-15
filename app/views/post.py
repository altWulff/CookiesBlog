from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse
from starlette_wtf import csrf_protect

from app.db import SessionLocal
from app.schemas import Post, PostCreate
from app.forms import NewPostForm
from app.config.jinja_env import templates, flash
import app.crud as crud

router = APIRouter()


@router.route('/post/new', methods=['GET', 'POST'])
@csrf_protect
async def create_new_post(request: Request):
    form = await NewPostForm.from_formdata(request)
    if await form.validate_on_submit():
        post = PostCreate(
            title=form.title.data,
            body=form.body.data,
        )
        db = SessionLocal()
        crud.post.create_with_user(db, post, user_id=1)
        flash(request, message='New post create', category='info')
        return RedirectResponse(url='/', status_code=303)

    return_status_code = 422 if form.errors else 200
    return templates.TemplateResponse(
        "post/new.html",
        {"request": request, 'form': form},
        status_code=return_status_code
    )
