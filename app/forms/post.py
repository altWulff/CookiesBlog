from starlette_wtf import StarletteForm
from wtforms import StringField, TextAreaField
from wtforms.validators import optional, length


class NewPostForm(StarletteForm):
    title = StringField(
        'Post Title'
    )
    body = TextAreaField('Post Body', [optional(), length(max=200)])
