#User form 

#Django 
from django import forms
from django.forms.fields import CharField
from django.forms.widgets import EmailInput 

#Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    username = forms.CharField(min_length=5, max_length=50)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=100, widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.CharField(min_length=6, max_length=60, widget=forms.EmailInput())

    #Username must be unique
    def clean_username(self):
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    #Verify password confirmation match
    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match")

        return data 

    #Create user and profile
    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user = user)
        profile.save()


class ProfileForm(forms.Form):
    website = forms.URLField(max_length = 200, required = True)
    biography = forms.CharField(max_length = 500, required = False)
    phone_number = forms.CharField(max_length = 20, required = False)
    picture = forms.ImageField()