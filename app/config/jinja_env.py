from fastapi import Request
from fastapi.templating import Jinja2Templates


def flash(request: Request, message: ..., category: str = "") -> None:
    if "_messages" not in request.session:
        request.session["_messages"] = []
    request.session["_messages"].append({"message": message, "category": category})


def get_flashed_messages(request: Request):
    print(request.session)
    return request.session.pop("_messages") if "_messages" in request.session else []


templates = Jinja2Templates(directory="templates")
templates.env.globals['get_flashed_messages'] = get_flashed_messages
