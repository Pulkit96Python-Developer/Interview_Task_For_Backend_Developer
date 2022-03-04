from django import forms
from captcha.fields import CaptchaField

class MyForm(forms.Form):
    Username=forms.CharField(max_length=20)
    First_Name=forms.CharField(max_length=50)
    Last_Name=forms.CharField(max_length=50)
    Email=forms.EmailField(max_length=50)
    Password=forms.CharField(widget=forms.PasswordInput)
    captcha=CaptchaField()


class AdminForm(forms.Form):
    Username=forms.CharField(max_length=20)
    Password=forms.CharField(max_length=10,widget=forms.PasswordInput)


class Edit_User_Form(forms.Form):
    Username=forms.CharField(max_length=20)
    First_Name=forms.CharField(max_length=50)
    Last_Name=forms.CharField(max_length=50)
    Email=forms.EmailField(max_length=50)
    Password=forms.CharField(widget=forms.PasswordInput)
