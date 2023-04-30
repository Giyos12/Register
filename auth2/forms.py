from django import forms
from django.core.exceptions import ValidationError


class StudentForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     p1 = self.cleaned_data["password1"]
    #     p2 = self.cleaned_data["password2"]
    #     if p1 != p2:
    #         raise ValidationError("bir xil emas")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
