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
                                   'required': '用户名不能为空',
                               },
                               widget=forms.TextInput(attrs={'placeholder': 'Please enter a username'}))

    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(label="Gender", choices=User.SEX_ITEMS)
    last_name = forms.CharField(label="Last Name", max_length=128)
    first_name = forms.CharField(label="First Name", max_length=128)
    usertype = forms.ChoiceField(label='User Type', choices=User.ROLES)

    email = forms.EmailField(label="Email Address",
                             widget=forms.TextInput(attrs={'placeholder': 'Required. Inform a valid email address.'}))

    password1 = forms.CharField(label='Password', min_length=8, max_length=256,
                                error_messages={
                                    'min_length': 'The password should be no less than 8 characters. ',
                                    'required': 'The password cannot be empty. ',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': 'Please enter the password.'}))

    password2 = forms.CharField(label='Password confirmation', min_length=8, max_length=256,
                                error_messages={
                                    'min_length': 'The password should be no less than 8 characters. ',
                                    'required': 'The password cannot be empty. ',
                                },
                                widget=forms.PasswordInput(attrs={'placeholder': 'Please confirm password.'}))

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

    error_messages = {'password_mismatch': '两次密码不一致', }

#
# class RegisterForm(forms.ModelForm):
#     error_messages = {
#         'password_mismatch': "The two password fields didn't match.",
#         'username_repeat': "The user name already exists. Please reselect the user name.",
#         'email_repeat': "This email address has been registered, please use another email.",
#     }
#
#     username = forms.CharField(label='Username', max_length=128,
#                                error_messages={
#                                    'required': '用户名不能为空',
#                                },
#                                widget=forms.TextInput(attrs={'placeholder': 'Please enter a username'}))
#
#     # age = forms.IntegerField(label="Age")
#     # gender = forms.ChoiceField(label="Gender", choices=User.SEX_ITEMS)
#     #
#     # last_name = forms.CharField(label="Last Name", max_length=128)
#     # first_name = forms.CharField(label="First Name", max_length=128)
#     # usertype = forms.ChoiceField(label='User Type', choices=User.ROLES)
#     email = forms.EmailField(label="Email Address",
#                              widget=forms.TextInput(attrs={'placeholder': 'Required. Inform a valid email address.'}))
#
#     password1 = forms.CharField(label='Password', min_length=8, max_length=256,
#                                 error_messages={
#                                     'min_length': 'The password should be no less than 8 characters. ',
#                                     'required': 'The password cannot be empty. ',
#                                 },
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Please enter the password.'}))
#
#     password2 = forms.CharField(label='Password confirmation', min_length=8, max_length=256,
#                                 error_messages={
#                                     'min_length': 'The password should be no less than 8 characters. ',
#                                     'required': 'The password cannot be empty. ',
#                                 },
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Please confirm password.'}))
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'age',
#             'gender',
#             'last_name',
#             'first_name',
#             'usertype',
#             'email',
#         )
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2
#
#     # def clean_username(self):
#     #     username = self.cleaned_data.get('username')
#     #     same_name_user = User.objects.filter(username=username)
#     #     if username == same_name_user:
#     #         raise forms.ValidationError(
#     #             self.error_messages['username_repeat'],
#     #             code='username_repeat',
#     #         )
#     #
#     # def clean_email(self):
#     #     email = self.cleaned_data.get('email')
#     #     same_email_user = User.objects.filter(email=email)
#     #     if email == same_email_user:
#     #         raise forms.ValidationError(
#     #             self.error_messages['email_repeat'],
#     #             code='email_repeat',
#     #         )
#
#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#
#         user.set_password(self.cleaned_data["password1"])
#
#         if commit:
#             user.save()
#         return user
