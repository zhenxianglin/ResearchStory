from django import forms

from Users.models import User


class LoginFom(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=128, unique=True)
    password = forms.CharField(label='create password', max_length=256)


class RegisterForm(forms.ModelForm):
    SEX_ITEMS = [
        (1, 'Male'),
        (2, 'Female'),
        (0, 'Secret'),
    ]

    ROLES = [
        (0, 'Researcher'),
        (1, 'Common User'),
    ]

    username = forms.CharField(label='Username', max_length=128, unique=True)
    age = forms.IntegerField(label="Age", null=True)
    gender = forms.IntegerField(label="Gender", choices=SEX_ITEMS)

    last_name = forms.CharField(label="Last Name", max_length=128)
    first_name = forms.CharField(label="First Name", max_length=128)
    usertype = forms.IntegerField(label='User Type', choices=ROLES)
    email = forms.EmailField(label="Email", unique=True)

    password1 = forms.CharField(label='create password', max_length=256)
    password2 = forms.CharField(abel='confirm password', max_length=256)
