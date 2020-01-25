from django import forms
from django.core import validators
from first_app.models import UserProfileInfo,Topic, Webpage, AccessRecord
from django.contrib.auth.models import User

# def check_for_z(value):
#     if value[0].lower =! "z":
#         raise forms.ValidationError("Names need to start with Z")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username','email','password']

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ['portfolio_site','profile_pic']

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label= "Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Email is not matching")
    
# class myNewForm(forms.ModelForm):
#     class Meta:
#         model = Webpage
#         fields = ["field1", "field2"]