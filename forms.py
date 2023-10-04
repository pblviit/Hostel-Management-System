from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField,DateField, SubmitField, ValidationError, RadioField, IntegerField
from wtforms.validators import DataRequired, Email, length

symbols = ' ~!@#$%^&*()_-+={[},}|\:,;"<,>.?/ '
nums = '1234567890'


def password_validation(form, field):
    if len(field.data) < 8:
        raise ValidationError("Password should be at least 8 characters long.")
    else:
        temp = False
        for i in symbols:
            if i in field.data:
                temp = True
        if temp == False:
            raise ValidationError("Use Special Charater.")
        else:
            temp = False
            for i in nums:
                if i in field.data:
                    temp = True
            if temp == False:
                raise ValidationError("Should contain Nums.")

def prn_validators(form, field):        
    if not field.data.isnumeric():
        raise ValidationError("Use Integer Only.")

class admin_form(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Login In")

class student_form(FlaskForm):
    prn_no = StringField("PRN No", validators=[DataRequired(), length(min = 8, max=8), prn_validators])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login In")

class registration_form(FlaskForm):
    Name = StringField("Name", validators=[DataRequired(), length(min=3, max=1999)])
    DOB = DateField("Date Of Birth", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    mobileno = StringField("Contact No", validators=[DataRequired(), length(min= 10,max=10), prn_validators])
    address = StringField("Address", validators=[DataRequired()])
    submit = SubmitField("Register")