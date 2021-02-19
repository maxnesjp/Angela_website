from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired(message="write something 😥...")])
    submit = SubmitField("Submit Comment")


class ContactForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired(message="Please enter your name.")])
    email_address = StringField(label="Email Address",
                                validators=[
                                    DataRequired(message="This field is required."),
                                ])
    phone_number = StringField(label="Phone Number")
    message_field = TextAreaField(label="Message",
                                  validators=[DataRequired(message="This field is required."), Length(max=200)])
    submit = SubmitField("Send")


class SecretKeyDownload(FlaskForm):
    key = StringField(label="Secret Code", validators=[DataRequired(message="This field is required.")])
    submit = SubmitField("Get Access to Resume")
