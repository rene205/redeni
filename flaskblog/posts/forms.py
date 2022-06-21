from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

#-----------------------------------Hier wird das Formular um Veröffentlichen von Kommentaren definiert ------------------------------------------
class PostForm(FlaskForm):
    title = StringField('Titel', validators=[DataRequired()])
    content = TextAreaField('Kommentar', validators=[DataRequired()])
    submit = SubmitField('Veröffentlichen')