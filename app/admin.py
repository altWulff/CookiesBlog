from sqladmin import ModelAdmin
from models import User, Post


class UserAdmin(ModelAdmin, model=User):
    column_list = [
        User.id,
        User.username,
        User.is_active,
        User.is_superuser,
        User.posts
    ]
