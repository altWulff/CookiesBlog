# Project Cookies Blog 
Develop a blog in `Python3`, with users, their posts, and pagination. As well as site search

## Libraries
- Written in `Python 3.10`
- At the heart of the back-end part of `FastAPI`
- Front-end template engine `Jinja2`
- NoSQL `MONGODB`

## Local launch of the project
`$ git clone git@github.com:altWulff/CookiesBlog.git && cd CookiesBlog`

`$ virtualenv venv`

`$ source venv/bin/activate`

`$ pip install -r requirements.txt`

`$ uvicorn app.app:app --reload`

Api documentation `http://127.0.0.1:8000/docs`

## Project Description
The main idea of the project: writing an API,
and a request to the end plates on the front-end template engine.

The project consists of the following blocks

1. Registration authentication and authorization of users
2. Admin panel for editing, deleting posts. Admin Only
3. Functionality for a blogger, creating, deleting, editing posts
4. Search created posts through search

### User types
The project provides for different levels of user access: Anonymous, User, Administrator
- Anonymous - has access to the main page, and can view the content of the posts. No need for registration
- User - has the same rights as Anonymous plus can edit his posts and delete them. Registration required
- Administrator - everything is the same as the user, plus he can delete and edit other people's posts. And also edit the data of other users
## The project is under development.


