from django import forms

class student(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField(max_length=20)
    suname = forms.CharField(max_length=20)
    spassword = forms.CharField(max_length=20,widget=forms.PasswordInput())
    semail = forms.EmailField()
