from django import forms
from blog.models import Commit


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commit
        fields = ['name', 'email', 'body', 'active']
