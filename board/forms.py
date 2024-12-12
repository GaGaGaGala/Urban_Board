from django import forms
from .models import Advertisement
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import photo


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('title', 'image')


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'content', 'author', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)