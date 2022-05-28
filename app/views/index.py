from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.api.post import list_posts
from app.config.jinja_env import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    posts = await list_posts()
    return templates.TemplateResponse(
        "index.html", {"request": request, "posts": posts}
    )
