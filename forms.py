from flask_wtf import FlaskForm, Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional

class dataForm(FlaskForm): 
    country = StringField('country', validators=[DataRequired()])
    per_capita = BooleanField('Per Capita?')
    submit = SubmitField('Get data')
