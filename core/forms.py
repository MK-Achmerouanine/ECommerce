from django import forms
from django.contrib.auth import get_user_model
class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email','password')