from django import forms
from .models import Post

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "image",
            "content",

        ]
