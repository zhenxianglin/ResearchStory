from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from Users.models import User


class LoginFom(forms.Form):
    username = forms.CharField(label='Username', max_length=128,
                               widget=forms.TextInput(attrs={'placeholder': 'Please enter your username'})
                               )
    password = forms.CharField(label='create password', max_length=256,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Please enter the password.'})
                               )


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=128,
                               error_messages={
                                   'required': 'Username can not be empty.',
                               },
                               widget=forms.TextInput(attrs={'placeholder': 'Please enter a username'}))

    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(label="Gender", choices=User.SEX_ITEMS)
    last_name = forms.CharField(label="Last Name", max_length=128)
    first_name = forms.CharField(label="First Name", max_length=128)
    usertype = forms.ChoiceField(label='User Type', choices=User.ROLES)

    email = forms.EmailField(label="Email Address",
                             widget=forms.TextInput(attrs={'placeholder': 'Required. Inform a valid email address.'})
                             )

    password1 = forms.CharField(label='Password', min_length=8, max_length=256,
                                error_messages={
                                    'min_length': 'The password should be no less than 8 characters. ',
                                    'required': 'The password cannot be empty. ',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': 'Please enter the password.'}),
                                help_text=(" - The password should be no less than 8 characters. <br/> - Your password can’t be too similar to your other personal information.<br/>  - Your password can’t be entirely numeric."),
                                )

    password2 = forms.CharField(label='Password confirmation', min_length=8, max_length=256,
                                error_messages={
                                    'min_length': 'The password should be no less than 8 characters. ',
                                    'required': 'The password cannot be empty. ',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': 'Please confirm password.'}),
                                help_text=(" - Enter the same password as above, for verification.\n"),
                                )

    class Meta:
        model = User
        fields = (
            'username',
            'age',
            'gender',
            'last_name',
            'first_name',
            'usertype',
            'email',
        )
