from .models import Profile
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices = Profile.ROLL_CHOICES)
    whatsapp_number = forms.CharField(required=True,widget=forms.TextInput)


    class Meta:
        model = User
        fields = ['username','email','password']
        help_texts = {
            'username' : None
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password does not match')
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()