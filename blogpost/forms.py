from .models import Comment
from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={
            'rows': '4',
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": "10",
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

class SearchForm(forms.Form):
    title_search = forms.CharField(max_length=20)

