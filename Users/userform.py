from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from Users.models import User, Profile


class LoginFom(forms.Form):
    """Create a Login form set to front-end through views function"""
    username = forms.CharField(label='Username', max_length=128,
                               widget=forms.TextInput(attrs={'placeholder': 'Please enter your username'})
                               )
    password = forms.CharField(label='create password', max_length=256,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Please enter the password.'})
                               )

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class RegisterForm(UserCreationForm):
    """generate a sign up form """
    username = forms.CharField(label='Username', max_length=128,
                               error_messages={
                                   'required': 'Username can not be empty.',
                               },
                               widget=forms.TextInput(attrs={'placeholder': 'Please enter a username'}))

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
                                help_text=(
                                    " - The password should be no less than 8 characters. <br/> - Your password can’t be too similar to your other personal information.<br/>  - Your password can’t be entirely numeric."),
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
            'usertype',
            'email',
            'password1',
            'password2',
        )

class ProfileForm(forms.ModelForm):
    """create a personal info editing form"""
    class Meta:
        model = Profile
        fields = ('age',
                  'gender',
                  'last_name',
                  'first_name',
                  'avatar',
                  'bio'
                  )
