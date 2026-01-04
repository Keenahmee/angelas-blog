from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, URL,Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

#Email()

class RegisterForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# TODO: Create a CommentForm so users can leave comments below posts

class CommentForm(FlaskForm):
    body=CKEditorField("Enter your Comment here")
    submit = SubmitField("Submit comment")