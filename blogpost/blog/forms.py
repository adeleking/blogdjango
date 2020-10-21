from django import forms
from .models import BlogModel

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = '__all__'



class BlogFormUpdate(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content']