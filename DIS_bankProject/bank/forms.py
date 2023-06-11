from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
# class AddCustomerForm(FlaskForm):
#     username = StringField('Username',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     password = PasswordField('Password', validators=[DataRequired()])
#     submit = SubmitField('Add')


class CustomerLoginForm(FlaskForm):
    id = IntegerField('CPR_number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# class TransferForm(FlaskForm):
#     amount = IntegerField('amount', 
#                         validators=[DataRequired()])
#     #sourceAccountTest = SelectField('From Account test:', choices=dropdown_choices, validators=[DataRequired()])
#     sourceAccount = SelectField('From Account:'  , choices=[], coerce = int, validators=[DataRequired()])
#     targetAccount = SelectField('Target Account:', choices=[], coerce = int, validators=[DataRequired()])
#     submit = SubmitField('Confirm')

# class DepositForm(FlaskForm):
#     amount = IntegerField('amount', 
#                        validators=[DataRequired()])
#     submit = SubmitField('Confirm')