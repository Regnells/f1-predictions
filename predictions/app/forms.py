from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class guessForm(FlaskForm):
    user = StringField('Användare', validators=[DataRequired()])
    race = StringField('Race', validators=[DataRequired()])
    first = StringField('Etta', validators=[DataRequired()])
    second = StringField('Tvåa', validators=[DataRequired()])
    third = StringField('Trea', validators=[DataRequired()])
    fourth = StringField('Fyra', validators=[DataRequired()])
    fifth = StringField('Femma', validators=[DataRequired()])
    sixth = StringField('Sexa', validators=[DataRequired()])
    submit = SubmitField('Tippa!')