from starlette_wtf import StarletteForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.widgets import PasswordInput
from wtforms.fields import EmailField


class RegisterUserForm(StarletteForm):
    username = StringField(
        'User name',
        validators=[DataRequired('Please enter your user name')]
    )
    email = EmailField(
        'Email address',
        validators=[
            DataRequired('Please enter your email address'),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        widget=PasswordInput(hide_value=False),
        validators=[
            DataRequired('Please enter your password'),
            EqualTo('password_confirm', message='Passwords must match')
        ]
    )

    password_confirm = PasswordField(
        'Confirm Password',
        widget=PasswordInput(hide_value=False),
        validators=[
            DataRequired('Please confirm your password')
        ]
    )


class LoginUserForm(StarletteForm):
    username = StringField(
        'User name',
        validators=[DataRequired('User name is required')]
    )
    email = EmailField(
        'Email address',
        validators=[
            DataRequired('Email address is required'),
            Email()
        ]
    )
