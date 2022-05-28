from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import JSONResponse

import app.crud as crud
from app.schemas import Post, PostUpdate

router = APIRouter()


@router.post("/", response_description="Add new post", response_model=Post)
async def create_post(user_id: str, post: Post = Body(...)):
    current_user_id = 0
    post = await crud.post.create_with_user(current_user_id, post)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=post)


@router.get("/", response_description="List all posts", response_model=list[Post])
async def list_posts(skip: int = 0, limit: int = 100):
    current_user_id = 0
    posts = await crud.post.get_multi_by_user(current_user_id, skip, limit)
    return posts


@router.get("/{post_id}", response_description="Get a single post", response_model=Post)
async def show_post(post_id: str):
    current_user_id = 0
    post = await crud.post.get(post_id)
    if post:
        return post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id=} not found"
    )


@router.put("/{post_id}", response_description="Update a post", response_model=Post)
async def update_post(post_id: str, post: PostUpdate = Body(...)):
    post = await crud.post.update(post_id, post)
    if post:
        return post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id=} not found"
    )


@router.delete("/{post_id}", response_description="Delete a post")
async def delete_student(post_id: str):
    delete_result = await crud.post.remove(post_id)
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {post_id=} not found"
    )
