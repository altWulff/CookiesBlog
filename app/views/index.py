from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from app.config.jinja_env import templates
from app.db.session import SessionLocal
from app.api.post import read_post


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    db = SessionLocal()
    posts = read_post(db)
    return templates.TemplateResponse(
        "index.html", {"request": request, 'posts': posts}
    )
