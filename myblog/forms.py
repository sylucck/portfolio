from .models import Comment
from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'rows': '2',
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": "2",
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class SearchForm(forms.Form):
    title = forms.CharField(max_length=20)

