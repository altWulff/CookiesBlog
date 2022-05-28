from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

import app.crud as crud
from app.schemas import User, UserUpdate

router = APIRouter()


@router.post("/", response_description="Add new user", response_model=User)
async def create_user(user: User = Body(...)):
    user = await crud.user.create(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=user)


@router.get("/", response_description="List all user", response_model=list[User])
async def list_users(skip: int = 0, limit: int = 100):
    users = await crud.user.get_multi(skip, limit)
    return users


@router.get("/{user_id}", response_description="Get a single user", response_model=User)
async def show_user(user_id: str):
    user = await crud.user.get(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id=} not found"
    )


@router.put("/{user_id}", response_description="Update a user", response_model=User)
async def update_user(user_id: str, user: UserUpdate = Body(...)):
    user = await crud.user.update(user_id, user)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id=} not found"
    )


@router.delete("/{user_id}", response_description="Delete a user")
async def delete_user(user_id: str):
    delete_result = await crud.user.remove(user_id)
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id=} not found"
    )
