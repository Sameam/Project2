from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import Users

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    telephone = IntegerField('Telephone', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_name(self, name):
        user = Users.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('This name already exists. Please use a different name.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email address has already been registered. Please use a different email address.')
    
    def validate_telephone(self, telephone):
        user = Users.query.filter_by(phone=telephone.data).first()
        if user is not None:
          raise ValidationError('This telephone has already been registered. Please use a different telephone.')
      
      
class editForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    score_1 = IntegerField('Score_1', validators=[DataRequired()])
    score_2 = IntegerField('Score_2', validators=[DataRequired()])
    score_3 = IntegerField('Score_3', validators=[DataRequired()])
    feedback = StringField('Feedback')
    submit = SubmitField('Confirm')
