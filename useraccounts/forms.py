from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import UserModel
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True, help_text='(Required)')
#     last_name = forms.CharField(max_length=30, required=False, help_text='(Optional)')
#     email = forms.EmailField(max_length=254, help_text='(Required)')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={}), 
        required=True, max_length=30
        )
    # user_profile_image = 
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_seller', 'description', 'user_profile_image']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        email = user.email
        try:
            validate_email(email)
        except ValidationError:
            forms.ValidationError('please write valid email address')
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'is_seller', 'description', 'user_profile_image']

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super(UserUpdateForm, self).save(commit=False)
            # user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user