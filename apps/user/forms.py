from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields[field].required:
                self.fields[field].help_text = '*Required'
        self.fields['email'].help_text = '*Required. Enter a valid email address.'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields[field].required:
                self.fields[field].help_text = '*Required'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AdminPasswordChangeCustomForm(AdminPasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(AdminPasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class SignupNextStep(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'updated_at', 'profile_photo', 'type', 'potential']

    def __init__(self, *args, **kwargs):
        super(SignupNextStep, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields[field].required:
                self.fields[field].help_text = '*Required'
        self.fields['broker'].label = 'Select a broker you wish to sign up'
        self.fields['referral_code'].label = 'Referral code (Enter NONE if you don\'t have one)'
