from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
# class AddCustomerForm(FlaskForm):
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Add')


class CustomerLoginForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TransferForm(FlaskForm):
    amount = IntegerField('amount', validators=[DataRequired()]) 
    sourceAccount = SelectField('From Account:'  , choices=[], validators=[DataRequired()])
    targetAccount = SelectField('Target Account:', choices=[], validators=[DataRequired()])
    submit = SubmitField('Confirm')