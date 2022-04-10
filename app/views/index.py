from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from config.jinja_env import templates


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
