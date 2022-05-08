from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired


class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    # category = SelectField(u'Pitch Category', choices=[('Product', 'Product'), ('Interview', 'Interview'), ('Life', 'Life')])
    category = SelectField(u'Pitch Category', choices=[('life', 'life'), ('Product', 'Product'), ('Interview', 'Interview')])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Help us know you better.',validators = [DataRequired()])
    submit = SubmitField('Submit')
