from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse
from app import app, csrf_protect
from schemas import Post, PostCreate
from forms import NewPostForm
from config.jinja_env import templates, flash


router = APIRouter()


@router.route('/post/new', methods=['GET', 'POST'])
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
