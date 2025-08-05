from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Comment


class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        fields=('username','email','password1','password2')
    


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_name','bio', 'image2', 'email']
        widgets = {
            'profile_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something...', 'rows': 3}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write a comment...'}),
        }
