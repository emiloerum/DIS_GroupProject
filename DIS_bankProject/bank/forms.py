from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


class CustomerLoginForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TransferForm(FlaskForm):
    amount = IntegerField('amount', validators=[DataRequired()]) 
    sourceAccount = SelectField('Source Account:'  , choices=[], coerce=int, validators=[DataRequired()])
    targetAccount = SelectField('Target Account:', choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Confirm')