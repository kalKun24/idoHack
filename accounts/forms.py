from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django import forms

class SignupForm(UserCreationForm): 
    class Meta:
        model = CustomUser
        fields = ('username',)
        
class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            ]
        